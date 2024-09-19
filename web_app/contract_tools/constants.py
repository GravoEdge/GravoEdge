from enum import Enum


class TokenParams(Enum):
    """
    Enum class to hold the token addresses for tokens
    """

    ETH: str = (
        "0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
        18,
    )
    STRK: str = (
        "0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
        18,
    )


class ProtocolAddress(Enum):

    zklend: str = "0x04c0a5193d58f74fbace4b74dcf65481e734ed1714121bdc571da345540efa05"
    nostra: str = "0x00c530f2c0aa4c16a0806365b0898499fba372e5df7a7172dc6fe9ba777e8007"
