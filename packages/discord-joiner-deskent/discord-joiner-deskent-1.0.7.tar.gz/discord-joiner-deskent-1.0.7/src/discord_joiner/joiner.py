import random
import re
import asyncio

import aiohttp
from base64 import b64encode

from myloguru import get_logger
from discord_joiner.exceptions import *


class DiscordJoiner:
    """
    Adds user token by invite link to discord server
    using proxy (optional)

        Attributes
        token: str
            Discord account token will be joined

        invite_link: str
            Invite link to channel

        log_level: int [Optional] = 20
            by default: 20 (INFO)

        proxy: str [Optional] = None
             example: proxy = "http": "http://user:pass@10.10.1.10:3128/"

        user_agent: str [Optional] =
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
        (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"

        delay: int [Optional] = 2
            Delay between requests, in seconds

        logger=None
            By default will be used my_loguru logger by Deskent

            (pip install myloguru-deskent)

    Methods
        join
            returns: bool
    """

    def __init__(
            self, token: str, invite_link: str, proxy: str = '',
            delay: float = 1, user_agent: str = '', log_level: int = 20,
            logger=None, timeout: int = 5
    ):
        self.token: str = token
        self.__headers: dict = {}
        self.__invite_link: str = invite_link
        self.session = aiohttp.ClientSession()
        self.timeout: int = timeout
        self.__locale: str = ''
        self.__invite_id: str = ''
        self._username: str = ""
        self._proxy: str = proxy
        self.fingerprint: str = ''
        self.__xsuperproperties: str = ''
        self.__delay: float = delay
        self.logger = logger if logger else get_logger(log_level)
        self.__user_agent = (
            user_agent
            if user_agent
            else ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/101.0.4951.41 Safari/537.36")
        )

    async def _check_proxy(self) -> bool:
        if not self._proxy:
            return True
        self.logger.debug("\n\tProxy checking...")
        params = {
            'url': "https://ifconfig.me/all.json",
            'proxy': self._proxy,
            'timeout': self.timeout
        }
        ip_address: list = re.findall(
            r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,6}\b',
            self._proxy
        )
        if not ip_address:
            raise ProxyError('Proxy address or port error')
        proxy_ip: str = ip_address[0]
        response: dict = await self.__send_request(params=params)
        result: bool = response.get('ip_addr', '') == proxy_ip.strip().split(':')[0]
        self.logger.debug(f"\n\tProxy checking... {result}")
        if not response:
            raise ProxyError('Proxy error: Response error')
        elif not result:
            raise ProxyError(f'Proxy {proxy_ip} is not valid.')

        return result

    async def __update_headers(self):
        self.__headers.update(
            {
                'user-agent': self.__user_agent, 'accept': '*/*',
                'accept-language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7',
                'content-type': 'application/json',
                'origin': 'https://discord.com', 'referer': self.__invite_link,
                'x-super-properties': self.__xsuperproperties
            }
        )

    async def __get_finger_print(self) -> None:
        params = {
            "url": "https://discord.com/api/v7/experiments"
        }
        response: dict = await self.__send_request(params)
        fingerprint = response.get("fingerprint")
        if not response or not fingerprint:
            self.logger.debug(f'\n\tFingerPrints: ERROR')
            raise FingerprintError
        self.fingerprint = fingerprint
        self.session.headers.update({'X-Fingerprint': fingerprint,
                                     'x-discord-locale': self.__locale,
                                     'authorization': self.token})
        self.logger.debug(f'\n\tFingerPrints: OK')

    async def __authorization(self) -> None:
        params = {
            "url": 'https://discordapp.com/api/v9/users/@me'
        }
        response: dict = await self.__send_request(params, cookies=True)
        result: dict = response.get('result', {})
        cookies = response.get('cookies', {})
        self._username = result.get('username', '')
        if not response or not cookies or not self._username:
            raise AuthorizationtError
        self.logger.debug(f'\n\tAuthorization: @{self._username}')
        self.session.headers['__sdcfduid'] = cookies.get('__sdcfduid').value

    async def __update_invite_id(self) -> None:
        self.__invite_id = self.__invite_link
        if not self.__invite_link.startswith(('https://discord.com/invite/', 'https://discord.gg')):
            raise InviteLinkError
        self.__invite_id = self.__invite_link.split('/')[-1]

    async def __get_xcontext_properties(self) -> None:
        params = {
            "url": f'https://discord.com/api/v7/invites/{self.__invite_id}',
        }
        data: dict = await self.__send_request(params)
        if not data:
            raise InviteLinkError
        location_guild_id = data['guild']['id']
        location_channel_id = data['channel']['id']

        base64_encode_data = b64encode(bytes(
            '{"location":"Accept Invite Page","location_guild_id":"'
            + str(location_guild_id)
            + '","location_channel_id":"'
            + str(location_channel_id)
            + '","location_channel_type":0}', 'utf-8'
        )).decode('utf-8')

        self.__headers['x-context-properties'] = base64_encode_data
        self.logger.debug("\n\tx-context-properties: OK")

    async def __join(self) -> None:
        params = {
            "url": f'https://discord.com/api/v7/invites/{self.__invite_id}',
            "json": {},
        }
        response: dict = await self.__send_request(params, method="post")
        code: int = response.get('code', 0)
        if not response:
            raise JoiningError
        if code == 40007:
            raise JoiningError(f'\n\tJoin: [@{self._username}] Ошибка при входе на канал, вы забанены на канале')
        channel_name = response['guild']['name']
        channel_id = response['guild']['id']
        text = (
            f'\n\tJoin: @{self._username} успешно вступил в канал {channel_name}'
            f'\n\tServer id: {channel_id}')
        self.logger.debug(text)

    async def __get_xsuperproperties(self) -> None:
        browser_version = str(self.__user_agent.split('Chrome/')[-1].split(' ')[0])
        self.__locale = random.choice(['za', 'et', 'ae', 'bh', 'dz', 'eg', 'iq', 'jo', 'kw', 'lb',
                                       'ly', 'ma',
                                       'cl', 'om', 'qa', 'sa', 'sd', 'sy', 'tn', 'ye', 'in', 'az',
                                       'ru', 'by',
                                       'bg', 'bd', 'in', 'cn', 'fr', 'es', 'fr', 'cz', 'gb', 'dk',
                                       'at', 'ch',
                                       'de', 'li', 'lu', 'de', 'mv', 'cy', 'gr', '029', 'au', 'bz',
                                       'ca', 'cb',
                                       'gb', 'ie', 'in', 'jm', 'mt', 'my', 'nz', 'ph', 'sg', 'tt',
                                       'us', 'za',
                                       'zw', 'ar', 'bo', 'cl', 'co', 'cr', 'do', 'ec', 'es', 'gt',
                                       'hn', 'mx',
                                       'ni', 'pa', 'pe', 'pr', 'py', 'sv', 'us', 'uy', 've', 'ee',
                                       'es', 'ir',
                                       'fi', 'ph', 'fo', 'be', 'ca', 'ch', 'fr', 'lu', 'mc', 'nl',
                                       'ie', 'gb',
                                       'ie', 'es', 'fr', 'in', 'il', 'in', 'ba', 'hr', 'de', 'hu',
                                       'am', 'id',
                                       'ng', 'cn', 'id', 'is', 'ch', 'it', 'il', 'jp', 'ge', 'kz',
                                       'gl', 'kh',
                                       'in', 'in', 'kr', 'kg', 'lu', 'la', 'lt', 'lv', 'nz', 'mk',
                                       'in', 'mn',
                                       'ca', 'in', 'bn', 'my', 'mt', 'no', 'np', 'be', 'nl', 'no',
                                       'no', 'za',
                                       'fr', 'in', 'in', 'pl', 'af', 'af', 'br', 'pt', 'gt', 'bo',
                                       'ec', 'pe',
                                       'ch', 'mo', 'ro', 'mo', 'ru', 'rw', 'ru', 'in', 'fi', 'no',
                                       'se', 'lk',
                                       'sk', 'si', 'no', 'se', 'no', 'se', 'fi', 'fi', 'al', 'ba',
                                       'cs', 'me',
                                       'rs', 'sp', 'fi', 'se', 'ke', 'sy', 'in', 'in', 'th', 'tm',
                                       'qs', 'za',
                                       'tr', 'ru', 'cn', 'ua', 'pk', 'uz', 'vn', 'sn', 'za', 'ng',
                                       'cn', 'hk',
                                       'mo', 'sg', 'tw', 'za'])
        self.__xsuperproperties: str = ''.join((
            '{"os":"Windows","browser":"Chrome","device":"","system_locale":"',
            self.__locale,
            '","browser_user_agent":"',
            self.__user_agent,
            '","browser_version":"',
            browser_version,
            '","os_version":"',
            str(random.choice(['7', '10', 'xp', 'vista', '11'])),
            (
                '","referrer":"https://www.yandex.ru/clck/jsredir?from=yandex.ru;suggest;browser&text=",'
                '"referring_domain":"www.yandex.ru",'
                '"referrer_current":"https://www.yandex.ru/clck/jsredir?from=yandex.ru;suggest;browser&text=",'
                '"referring_domain_current":"www.yandex.ru","release_channel":"stable","client_build_number":'
            ),
            str(random.randint(100000, 199999)),
            ',"client_event_source":null}'
        ))

    async def __send_request(self, params: dict, method: str = "get", cookies: bool = False) -> dict:
        await asyncio.sleep(self.__delay)

        if self._proxy:
            params.update(proxy=self._proxy)
        params.update(ssl=False, timeout=self.timeout)
        async with self.session.request(method=method, **params) as response:
            response_text: str = await response.text()
            self.logger.debug(response_text)
            result: dict = await response.json()
            captcha_key: str = result.get("captcha_sitekey")
            if captcha_key:
                raise JoinerBaseException(text="Captcha error.")
            message: str = result.get("message", '')
            if message == "You need to verify your account in order to perform this action.":
                raise JoinerBaseException(text=message)
            sleep_time = float(result.get('retry_after', 0))
            if sleep_time:
                self.logger.debug(f'Cooldown, sleeping for {sleep_time} seconds.')
                raise CooldownError(f'Cooldown, sleeping for {sleep_time} seconds.')
            if cookies:
                result = {'result': result, 'cookies': response.cookies}

        return result

    async def join(self) -> dict:
        """Add user with token to server by invite link

        :returns: dict {'success': True, 'token': token} if done
        else {'success': False, 'token': token, 'message': ...}
        """

        self.logger.debug(f'TOKEN: {self.token}:')
        result = {'success': False, 'token': self.token}
        if not self.session.closed:
            await self.session.close()
        async with aiohttp.ClientSession(headers=self.__headers) as session:
            self.session = session
            try:
                await self.__update_invite_id()
                await self._check_proxy()
                await self.__get_xsuperproperties()
                await self.__update_headers()
                await self.__get_finger_print()
                await self.__authorization()
                await self.__get_xcontext_properties()
                await self.__join()
            except JoinerBaseException as err:
                self.logger.error(err)
                message = err.text
                result.update(message=message)

                return result
            except Exception as err:
                self.logger.error(err)
                result.update(message=err)
                return result

            result.update(success=True)
            return result
