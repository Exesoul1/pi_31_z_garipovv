from abc import ABC, abstractmethod


# Разбиваем интерфейс на маленькие по ролям
class Printable(ABC):
    @abstractmethod
    def print(self, text: str) -> None:
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass

class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str) -> None:
        pass


class Copiable(ABC):
    @abstractmethod
    def copy(self) -> None:
        pass


class SimplePrinter(Printable):
    def print(self, text: str) -> None:
        print(f"Печатаю: {text}")
    # Методов scan/fax/copy здесь нет — они не нужны этому устройству


def send_to_print(device: Printable, text: str) -> None:
    device.print(text)

# Пример использования
if __name__ == "__main__":
    printer = SimplePrinter()
    send_to_print(printer, "Отчёт.pdf")
