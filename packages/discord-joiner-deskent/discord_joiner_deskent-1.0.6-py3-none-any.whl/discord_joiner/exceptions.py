class CooldownError(Exception):
    def __str__(self):
        return 'Request cooldown error'


class FingerprintError(Exception):
    def __str__(self):
        return 'Fingerprint error'


class AuthorizationtError(Exception):
    def __str__(self):
        return 'Authorization Error: Invalid token'


class InviteLinkError(Exception):
    def __str__(self):
        return 'Invite link is not valid'


class JoiningError(Exception):
    def __str__(self):
        return 'Joining error'


class ProxyError(Exception):
    def __str__(self):
        return 'Proxy error'
