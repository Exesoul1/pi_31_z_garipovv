from abc import ABC, abstractmethod

class Notifier(ABC):
    def __init__(self, recipient: str):
        self.recipient = recipient

    @abstractmethod
    def send(self, message: str) -> None:
        pass

    @classmethod
    @abstractmethod
    def create_notification(cls, recipient: str) -> "Notifier":
        pass

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email → {self.recipient}: {message}")

    @classmethod
    def create_notification(cls, recipient: str) -> "Notifier":
        return cls(recipient)

class SmsNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"SMS → {self.recipient}: {message}")

    @classmethod
    def create_notification(cls, recipient: str) -> "Notifier":
        return cls(recipient)

class PushNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Push → {self.recipient}: {message}")

    @classmethod
    def create_notification(cls, recipient: str) -> "Notifier":
        return cls(recipient)

# Фабрика: выбирает класс по названию канала
class NotifierFactory:
    _registry = {
        "email": EmailNotifier,
        "sms": SmsNotifier,
        "push": PushNotifier,
    }

    @classmethod
    def create(cls, channel: str, recipient: str) -> Notifier:
        notifier_class = cls._registry.get(channel)
        if not notifier_class:
            raise ValueError(f"Неизвестный канал: {channel}")
        return notifier_class.create_notification(recipient)


def notify(channel: str, target: str, message: str) -> None:
    notifier = NotifierFactory.create(channel, target)
    notifier.send(message)

# Пример
if __name__ == "__main__":
    notify("email", "user@example.com", "Ваш заказ подтверждён")
    notify("sms", "+79001234567", "Код подтверждения: 1234")
