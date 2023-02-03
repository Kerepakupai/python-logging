import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = "logs3.papertrailapp.com"
PAPERTRAIL_PORT = 50813


def main() -> None:
    logger = logging.getLogger("kerepakupai")
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)

    logger.debug("This is a debug message")

if __name__ == "__main__":
    main()
