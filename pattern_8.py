from abc import ABC, abstractmethod


class Toast(ABC):
    @abstractmethod
    def show(self, message: str) -> None: pass


class Dialog(ABC):
    @abstractmethod
    def show(self, title: str, body: str, buttons: list[str]) -> None: pass


class ProgressBar(ABC):
    @abstractmethod
    def show(self, label: str, value: int) -> None: pass


# iOS компоненты
class IosToast(Toast):
    def show(self, message: str) -> None: print(f"[iOS Toast] {message}")


class IosDialog(Dialog):
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        print(f"[iOS Dialog] {title}: {body} ({', '.join(buttons)})")

class IosProgressBar(ProgressBar):
    def show(self, label: str, value: int) -> None: print(f"[iOS Progress] {label}: {value}%")


# Android компоненты
class AndroidToast(Toast):
    def show(self, message: str) -> None: print(f"[Android Toast] {message}")


class AndroidDialog(Dialog):
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        print(f"[Android Dialog] {title}: {body} ({', '.join(buttons)})")


class AndroidProgressBar(ProgressBar):
    def show(self, label: str, value: int) -> None: print(f"[Android Progress] {label}: {value}%")


# Абстрактная фабрика
class NotificationFactory(ABC):
    @abstractmethod
    def create_toast(self) -> Toast: ...
    @abstractmethod
    def create_dialog(self) -> Dialog: ...
    @abstractmethod
    def create_progress_bar(self) -> ProgressBar: ...


class IosFactory(NotificationFactory):
    def create_toast(self) -> Toast: return IosToast()
    def create_dialog(self) -> Dialog: return IosDialog()
    def create_progress_bar(self) -> ProgressBar: return IosProgressBar()


class AndroidFactory(NotificationFactory):
    def create_toast(self) -> Toast: return AndroidToast()
    def create_dialog(self) -> Dialog: return AndroidDialog()
    def create_progress_bar(self) -> ProgressBar: return AndroidProgressBar()


def show_upload_progress(factory, filename: str, progress: int):
    toast = factory.create_toast()
    bar   = factory.create_progress_bar()

    toast.show(f"Загрузка {filename} начата")
    bar.show("Прогресс загрузки", progress)

    if progress == 100:
        dialog = factory.create_dialog()
        dialog.show("Готово", f"{filename} успешно загружен", ["OK"])


if __name__ == "__main__":
    show_upload_progress(IosFactory(), "photo.jpg", 50)
    show_upload_progress(IosFactory(), "photo.jpg", 100)

    print("-" * 20)

    show_upload_progress(AndroidFactory(), "document.pdf", 75)
    show_upload_progress(AndroidFactory(), "document.pdf", 100)
