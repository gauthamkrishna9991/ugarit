from os import environ
from typing import Any, Dict


class ServerConfig:
    """
    # Server Config
    """

    _debug: str = "debug"
    debug: bool

    def __init__(self, debug: bool) -> None:
        self.debug = debug

    @staticmethod
    def cli_parse(cli_args: Dict[str, Any]) -> "ServerConfig":
        return ServerConfig(cli_args[ServerConfig._debug])
