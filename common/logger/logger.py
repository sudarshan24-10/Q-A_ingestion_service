import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from threading import Lock


class AppLogger:
    _instance = None
    _lock = Lock()

    def __new__(cls, log_file: str = "logs/app.log"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_logger(log_file)
        return cls._instance

    def _init_logger(self, log_file: str):
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger("app")
        self.logger.setLevel(logging.INFO)

        if self.logger.handlers:
            return

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler = RotatingFileHandler(
            log_file, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
        )
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)
        self.logger.propagate = False

    def get_logger(self):
        return self.logger
