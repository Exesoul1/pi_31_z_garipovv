from abc import ABC, abstractmethod
from datetime import datetime


class Logger(ABC):
    @abstractmethod
    def info(self, message: str) -> None: pass

    @abstractmethod
    def warning(self, message: str) -> None: pass

    @abstractmethod
    def error(self, message: str, exception: Exception = None) -> None: pass


class MonologLogger:
    def __init__(self, channel: str):
        self.channel = channel

    def add_record(self, level: str, msg: str, context: dict = None) -> None:
        ts = datetime.now().strftime("%H:%M:%S")
        ctx = f" {context}" if context else ""
        print(f"[{ts}] {self.channel}.{level}: {msg}{ctx}")

    def push_handler(self, handler_name: str) -> None:
        print(f"[Monolog] Handler '{handler_name}' registered")


class MonologAdapter(Logger):
    def __init__(self, monolog: MonologLogger):
        self._monolog = monolog

    def info(self, message: str) -> None:
        self._monolog.add_record("INFO", message)

    def warning(self, message: str) -> None:
        self._monolog.add_record("WARNING", message)

    def error(self, message: str, exception: Exception = None) -> None:
        context = {"exception": str(exception)} if exception else None
        self._monolog.add_record("ERROR", message, context)


def process_order(logger: Logger, order_id: int):
    logger.info(f"Обработка заказа #{order_id}")
    try:
        if order_id < 0:
            raise ValueError("ID не может быть отрицательным")
        logger.info(f"Заказ #{order_id} успешно обработан")
    except ValueError as e:
        logger.error("Ошибка обработки заказа", exception=e)


if __name__ == "__main__":
    process_order(MonologAdapter(MonologLogger("app")), 42)
    process_order(MonologAdapter(MonologLogger("app")), -1)
