from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Order:
    total: float

@dataclass
class Customer:
    kind: str

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, order: Order, customer: Customer) -> float:
        pass

class RegularDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total

class VIPDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total * 0.9

class EmployeeDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total * 0.8

# Новая скидка 
class BlackFridayDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total * 0.7

DISCOUNT_REGISTRY: dict[str, DiscountStrategy] = {
    "regular": RegularDiscount(),
    "vip": VIPDiscount(),
    "employee": EmployeeDiscount(),
    "black_friday": BlackFridayDiscount(),
}


def apply_discount(order: Order, customer: Customer) -> float:
    strategy = DISCOUNT_REGISTRY.get(customer.kind)
    if strategy:
        return strategy.apply(order, customer)
    return order.total


if __name__ == "__main__":
    order = Order(total=100.0)
    for kind in ["regular", "vip", "employee", "black_friday", "unknown"]:
        cust = Customer(kind=kind)
        print(f"{kind:>12} | итого: {apply_discount(order, cust):.2f}")
