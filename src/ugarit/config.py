import os
from typing import Any, Dict


class ServerConfig:
    """
    # Server Config
    """

    _debug: str = "debug"
    debug: bool = os.environ["DEBUG"] == "1" if "DEBUG" in os.environ else False

    def __init__(self, debug: bool) -> None:
        self.debug = debug

    @staticmethod
    def cli_parse(cli_args: Dict[str, Any]) -> "ServerConfig":
        return ServerConfig(cli_args[ServerConfig._debug])
