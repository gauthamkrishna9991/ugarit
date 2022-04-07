# Standard Libraries
import argparse

# Uvicorn Run App
from uvicorn import run

# Package Imports

# Import App
from ugarit.app import app
from ugarit.config import ServerConfig

# Application Name
APP_NAME = "ugarit.app:app"

# Main Application
def main():
    """
    # Main Function
    """
    # Initialize Parser
    parser = argparse.ArgumentParser(
        description="Main Server Application", exit_on_error=1
    )
    # Run Argument (--run/-r)
    parser.add_argument(
        "--run",
        "-r",
        action="store_true",
        help="Run Server Application",
    )
    # Debug Argument (--debug/-d)
    parser.add_argument(
        "--debug", "-d", action="store_true", help="Enable Debug Version"
    )
    # Parse Arguments
    args = parser.parse_args()

    # If command to run is given
    if args.run:
        config_args = {"debug": args.debug}
        config: ServerConfig = ServerConfig.cli_parse(config_args)
        if config.debug:
            run(APP_NAME, debug=config.debug, reload=config.debug)
        else:
            run(app)
    else:
        parser.print_help()
