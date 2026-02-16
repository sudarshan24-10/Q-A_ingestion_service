# common/logger/span.py
import time
from common.logger.logger import AppLogger


class Span:
    def __init__(self, name: str):
        self.name = name
        self.logger = AppLogger().get_logger()

    def __enter__(self):
        self.start = time.perf_counter()
        self.logger.info(f"[SPAN] ▶ {self.name} started")
        return self

    def __exit__(self, exc_type, exc, tb):
        duration = time.perf_counter() - self.start
        self.logger.info(f"[SPAN] ◀ {self.name} took {duration:.4f}s")
