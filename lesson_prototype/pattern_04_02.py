from abc import ABC, abstractmethod
from copy import deepcopy


class Cloneable(ABC):
    @abstractmethod
    def clone(self): pass


class Button(Cloneable):
    def __init__(self, label: str, color: str, size: str, disabled: bool = False):
        self.label = label
        self.color = color
        self.size = size
        self.disabled = disabled

    def clone(self) -> 'Button':
        return deepcopy(self)

    def __str__(self) -> str:
        state = "выкл." if self.disabled else "вкл."
        return f"Button[{self.size}] '{self.label}' ({self.color}, {state})"


class Card(Cloneable):
    def __init__(self, title: str, tags: list[str], elevation: int = 1):
        self.title = title
        self.tags = tags
        self.elevation = elevation

    def clone(self) -> 'Card':
        return deepcopy(self)

    def __str__(self) -> str:
        return f"Card '{self.title}' tags={self.tags} elevation={self.elevation}"


class ComponentRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, name: str, prototype: Cloneable):
        self._prototypes[name] = prototype

    def get(self, name: str) -> Cloneable:
        if name not in self._prototypes:
            raise ValueError(f"Прототип '{name}' не найден")
        return self._prototypes[name].clone()


if __name__ == "__main__":
    registry = ComponentRegistry()
    registry.register("primary_btn", Button("ОК", "blue", "md"))
    registry.register("danger_btn", Button("Удалить", "red", "sm"))
    registry.register("article_card", Card("Новость", ["tech", "news"], elevation=2))

    btn1 = registry.get("primary_btn")
    btn1.label = "Подтвердить"
    btn2 = registry.get("primary_btn")

    print(btn1)
    print(btn2)
