"""
SSH configuration tokens to use in certain configuration settings

Tokens are described on the manual sshd manual page in TOKENS section.
"""

from enum import Enum


class Token(Enum):
    """
    SSH server configuration string token
    """
    HOME = '%h'
    KEY_ID = '%i'
    USER_ID = '%U'
    USERNAME = '%u'
    CA_KEY_FINGERPRINT = '%F'
    CA_KEY_BASE64 = '%K'
    CA_KEY_TYPE = '%T'
    CERTIFICATE_SERIAL_NUMBER = '%s'
    CERTIFICATE_FINGERPRINT = '%f'
    CERTIFICATE_BASE64 = '%k'
    CERTIFICATE_TYPE = '%t'
    PERCENT = '%%'
    ROUTING_DOMAIN = '%D'


FILE_PATH_TOKENS = (
    Token.PERCENT,
    Token.HOME,
    Token.USER_ID,
    Token.USERNAME,
)

AUTHORIZED_PRINCIPALS_TOKENS = (
    Token.HOME,
    Token.KEY_ID,
    Token.USER_ID,
    Token.USERNAME,
    Token.CA_KEY_FINGERPRINT,
    Token.CA_KEY_BASE64,
    Token.CA_KEY_TYPE,
    Token.CERTIFICATE_SERIAL_NUMBER,
    Token.CERTIFICATE_FINGERPRINT,
    Token.CERTIFICATE_BASE64,
    Token.CERTIFICATE_TYPE,
    Token.PERCENT,
)

AUTHORIZED_KEYS_COMMAND_TOKENS = (
    Token.PERCENT,
    Token.HOME,
    Token.USER_ID,
    Token.USERNAME,
    Token.CERTIFICATE_FINGERPRINT,
    Token.CERTIFICATE_BASE64,
    Token.CERTIFICATE_TYPE,
)

ROUTING_DOMAIN_TOKENS = (
    Token.ROUTING_DOMAIN,
)

AUTHORIZED_PRONCIPALS_FILE_TOKENS = FILE_PATH_TOKENS
AUTHORIZED_KEYS_FILE_TOKENS = FILE_PATH_TOKENS
CHROOT_DIRECTORY_TOKENS = FILE_PATH_TOKENS
