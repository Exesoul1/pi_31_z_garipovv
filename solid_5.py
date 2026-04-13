from abc import ABC, abstractmethod
from typing import List

# Абстрактный интерфейс
class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, text: str) -> None:
        pass


class EmailClient(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[EMAIL to={to}] {text}")

class SmsClient(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[SMS to={to}] {text}")



class NotificationService:
    def __init__(self, notifiers: List[Notifier]):
        self.notifiers = notifiers

    def notify(self, to: str, text: str) -> None:
        for notifier in self.notifiers:
            notifier.send(to, text)

# Пример использования
if __name__ == "__main__":
    # 1. Создаем сервис с нужными каналами
    service = NotificationService([EmailClient(), SmsClient()])
    service.notify("user@example.com", "Ваш код: 1234")

    # 2. Добавляем Push-уведомления 
    class PushNotifier(Notifier):
        def send(self, to: str, text: str) -> None:
            print(f"[PUSH to={to}] {text}")

    service_with_push = NotificationService([EmailClient(), PushNotifier()])
    service_with_push.notify("user@example.com", "Новое сообщение")


    class FakeNotifier(Notifier):
        def send(self, to: str, text: str) -> None:
            pass  

    test_service = NotificationService([FakeNotifier()])
    test_service.notify("test@example.com", "Тест")
