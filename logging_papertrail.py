import logging
from logging.handlers import SysLogHandler
import os


PAPERTRAIL_HOST = os.environ["PAPERTRAIL_HOST"]
PAPERTRAIL_PORT = os.environ["PAPERTRAIL_PORT"]


def main() -> None:
    logger = logging.getLogger("kerepakupai")
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)

    logger.debug("This is a debug message")

if __name__ == "__main__":
    main()
