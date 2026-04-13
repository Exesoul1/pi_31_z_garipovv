from abc import ABC, abstractmethod


class Hero(ABC):
    @abstractmethod
    def describe(self) -> str: ...
    @abstractmethod
    def attack(self, weapon) -> str: ...


class Enemy(ABC):
    @abstractmethod
    def describe(self) -> str: ...
    @abstractmethod
    def health(self) -> int: ...


class Weapon(ABC):
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def damage(self) -> int: ...


# Фэнтези семейство
class FantasyHero(Hero):
    def describe(self) -> str: return "Рыцарь в латах"
    def attack(self, weapon) -> str: return f"Рыцарь бьёт {weapon.name()} ({weapon.damage()} урона)"


class FantasyEnemy(Enemy):
    def describe(self) -> str: return "Дракон"
    def health(self) -> int: return 500


class FantasyWeapon(Weapon):
    def name(self) -> str: return "Стальной меч"
    def damage(self) -> int: return 45


# Sci-Fi семейство
class SciFiHero(Hero):
    def describe(self) -> str: return "Космодесантник"
    def attack(self, weapon) -> str: return f"Десантник стреляет из {weapon.name()} ({weapon.damage()} урона)"


class SciFiEnemy(Enemy):
    def describe(self) -> str: return "Боевой робот"
    def health(self) -> int: return 300


class SciFiWeapon(Weapon):
    def name(self) -> str: return "Лазерная винтовка"
    def damage(self) -> int: return 60


# Абстрактная фабрика
class WorldFactory(ABC):
    @abstractmethod
    def create_hero(self) -> Hero: ...
    @abstractmethod
    def create_enemy(self) -> Enemy: ...
    @abstractmethod
    def create_weapon(self) -> Weapon: ...


class FantasyFactory(WorldFactory):
    def create_hero(self) -> Hero: return FantasyHero()
    def create_enemy(self) -> Enemy: return FantasyEnemy()
    def create_weapon(self) -> Weapon: return FantasyWeapon()


class SciFiFactory(WorldFactory):
    def create_hero(self) -> Hero: return SciFiHero()
    def create_enemy(self) -> Enemy: return SciFiEnemy()
    def create_weapon(self) -> Weapon: return SciFiWeapon()


def create_world(factory):
    hero   = factory.create_hero()
    enemy  = factory.create_enemy()
    weapon = factory.create_weapon()

    print(f"Герой: {hero.describe()}")
    print(f"Враг: {enemy.describe()} (здоровье: {enemy.health()})")
    print(hero.attack(weapon))


if __name__ == "__main__":
    create_world(FantasyFactory())
    print("-" * 30)
    create_world(SciFiFactory())
