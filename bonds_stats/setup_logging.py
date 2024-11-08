import logging
from logging.handlers import RotatingFileHandler
import configparser
import os

def setup_logging(config_path="config.ini"):
    # Читаем конфигурацию из файла config.ini
    config = configparser.ConfigParser(interpolation=None)
    if not os.path.exists(config_path):
        print("Config file not found. Using default logging settings.")
        config['logging'] = {}
    
    config.read(config_path)

    # Настройки логгера
    log_level = getattr(logging, config.get("logging", "log_level", fallback="INFO").upper())
    log_format = config.get("logging", "log_format", fallback="%(asctime)s - %(levelname)s - %(message)s")

    log_to_file = config.getboolean("logging", "log_to_file", fallback=True)
    log_to_console = config.getboolean("logging", "log_to_console", fallback=True)

    handlers = []

    if log_to_file:
        log_file = config.get("logging", "log_file", fallback="app.log")
        log_file_encoding = config.get("logging", "log_file_encoding", fallback="utf-8")
        max_log_file_size = config.getint("logging", "max_log_file_size", fallback=1048576)
        backup_count = config.getint("logging", "backup_count", fallback=3)

        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_log_file_size, backupCount=backup_count, encoding=log_file_encoding
        )
        file_handler.setFormatter(logging.Formatter(log_format))
        handlers.append(file_handler)

    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(log_format))
        handlers.append(console_handler)

    logging.basicConfig(
        level=log_level,
        handlers=handlers
    )

    logger = logging.getLogger(__name__)
    return logger