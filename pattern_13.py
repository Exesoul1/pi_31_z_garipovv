class Pizza:
    def __init__(self):
        self.size: str = ""
        self.dough: str = ""
        self.sauce: str = ""
        self.cheese: str = ""
        self.toppings: list[str] = []


    def __str__(self) -> str:
        toppings = ', '.join(self.toppings) if self.toppings else 'без топпингов'
        return (
            f"Пицца {self.size} на {self.dough} тесте\n"
            f"Соус: {self.sauce}, Сыр: {self.cheese}\n"
            f"Топпинги: {toppings}"
        )


# Строитель пиццы
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()


    def set_size(self, size: str):
        self.pizza.size = size
        return self


    def set_dough(self, dough: str):
        self.pizza.dough = dough
        return self


    def set_sauce(self, sauce: str):
        self.pizza.sauce = sauce
        return self


    def set_cheese(self, cheese: str):
        self.pizza.cheese = cheese
        return self


    def add_topping(self, topping: str):
        self.pizza.toppings.append(topping)
        return self


    def build(self) -> Pizza:
        if not self.pizza.size or not self.pizza.dough:
            raise ValueError("Размер и тип теста — обязательные параметры")
        return self.pizza


class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder


    def build_margherita(self) -> Pizza:
        return (
            self.builder
            .set_size("M")
            .set_dough("тонком")
            .set_sauce("томатный")
            .set_cheese("моцарелла")
            .add_topping("базилик")
            .build()
        )


    def build_pepperoni(self) -> Pizza:
        return (
            self.builder
            .set_size("L")
            .set_dough("классическом")
            .set_sauce("томатный")
            .set_cheese("моцарелла")
            .add_topping("пепперони")
            .add_topping("чили")
            .build()
        )


    def build_vegetarian(self) -> Pizza:
        return (
            self.builder
            .set_size("M")
            .set_dough("цельнозерновом")
            .set_sauce("песто")
            .set_cheese("фета")
            .add_topping("помидоры")
            .add_topping("оливки")
            .add_topping("грибы")
            .build()
        )


# Пример
if __name__ == "__main__":
    director = Director(PizzaBuilder())


    print(director.build_margherita())
    print("-" * 30)
    print(director.build_pepperoni())
    print("-" * 30)
    print(director.build_vegetarian())
    print("-" * 30)

    custom = (
        PizzaBuilder()
        .set_size("XL")
        .set_dough("пышном")
        .set_sauce("сливочный")
        .set_cheese("чеддер")
        .add_topping("бекон")
        .add_topping("ананас")
        .build()
    )
    print(custom)

    # Проверка валидации: раскомментируйте, чтобы увидеть ошибку
    # PizzaBuilder().set_size("M").build()  # ValueError: нет теста
