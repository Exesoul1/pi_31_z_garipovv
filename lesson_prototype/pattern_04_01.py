import copy
from dataclasses import dataclass, field


@dataclass
class Stats:
    hp: int
    attack: int
    defense: int


@dataclass
class Ability:
    name: str
    damage: int
    cooldown: float


class Character:
    def __init__(self, name: str, level: int, stats: Stats, abilities: list[Ability]):
        self.name = name
        self.level = level
        self.stats = stats
        self.abilities = abilities


    def __str__(self) -> str:
        abilities = ', '.join(a.name for a in self.abilities)
        return (
            f"{self.name} (ур.{self.level}) | "
            f"HP:{self.stats.hp} ATK:{self.stats.attack} | "
            f"Способности: {abilities}"
        )


    def clone(self) -> "Character":
        return copy.deepcopy(self)


# Проверка:
original = Character(
    name="Воин",
    level=10,
    stats=Stats(hp=200, attack=50, defense=30),
    abilities=[Ability("Удар меча", 80, 1.5), Ability("Щитовой блок", 0, 3.0)],
)

clone = original.clone()
clone.name = "Воин-клон"
clone.stats.hp = 150
clone.abilities[0].damage = 999

print(original)
print(clone)
