from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Input(ABC):
    @abstractmethod
    def render(self) -> str: ...


# Виджеты светлой темы
class LightButton(Button):
    def render(self) -> str: return "[Light Button]"
class LightCheckbox(Checkbox):
    def render(self) -> str: return "[Light Checkbox]"
class LightInput(Input):
    def render(self) -> str: return "[Light Input]"


# Виджеты тёмной темы
class DarkButton(Button):
    def render(self) -> str: return "[Dark Button]"
class DarkCheckbox(Checkbox):
    def render(self) -> str: return "[Dark Checkbox]"
class DarkInput(Input):
    def render(self) -> str: return "[Dark Input]"


# Абстрактная фабрика: создаёт целое семейство виджетов
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...
    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...
    @abstractmethod
    def create_input(self) -> Input: ...


class LightThemeFactory(UIFactory):
    def create_button(self) -> Button: return LightButton()
    def create_checkbox(self) -> Checkbox: return LightCheckbox()
    def create_input(self) -> Input: return LightInput()


class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button: return DarkButton()
    def create_checkbox(self) -> Checkbox: return DarkCheckbox()
    def create_input(self) -> Input: return DarkInput()



class Application:
    def __init__(self, factory: UIFactory):
        self.factory = factory


    def render_ui(self):
        btn = self.factory.create_button()
        chk = self.factory.create_checkbox()
        inp = self.factory.create_input()
        print(btn.render(), chk.render(), inp.render())


if __name__ == "__main__":
    app = Application(DarkThemeFactory())
    app.render_ui()
