#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
config

Application Configuration Module

This holds application configuration required for server.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
# OS Imports
import os

# Typing Imports
from typing import Any, Dict

# -- CLASS


# pylint: disable=too-few-public-methods
class ServerConfig:
    """
    # Server Config
    """

    _debug: str = "debug"
    _logfile: str = "logfile"
    debug: bool = os.environ["DEBUG"] == "1" if "DEBUG" in os.environ else False
    logfile: str = os.environ["LOGFILE"] if "LOGFILE" in os.environ else "ugarit.log"

    def __init__(self, debug: bool) -> None:
        self.debug = debug

    @staticmethod
    def cli_parse(cli_args: Dict[str, Any]) -> "ServerConfig":
        """
        cli_parse

        Pass Configuration Arguments
        """
        return ServerConfig(cli_args[ServerConfig._debug])
