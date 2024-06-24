import os
import logging

FORMAT = '%(asctime)s,%(msecs)03d - %(levelname)s - %(message)s'


def get_logger(module_name: str) -> logging.Logger:
    logger = logging.getLogger(module_name)

    level_str = os.getenv("LOG_LEVEL", "ERROR")
    if level_str == "ERROR":
        level = logging.ERROR
    elif level_str == "WARN":
        level = logging.WARN
    elif level_str == "INFO":
        level = logging.INFO
    elif level_str == "DEBUG":
        level = logging.DEBUG
    else:
        raise EnvironmentError("Incorrect log level environment variable")

    logging.basicConfig(level=level, format=FORMAT)
    return logger