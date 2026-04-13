from abc import ABC, abstractmethod


class Gateway(ABC):
    @abstractmethod
    def pay(self, amount: float, currency: str) -> str: ...
    @abstractmethod
    def refund(self, transaction_id: str) -> str: ...


class StripeGateway(Gateway):
    def pay(self, amount: float, currency: str) -> str: return f"Stripe: списано {amount} {currency}"
    def refund(self, transaction_id: str) -> str: return f"Stripe: возврат {transaction_id}"


class PayPalGateway(Gateway):
    def pay(self, amount: float, currency: str) -> str: return f"PayPal: списано {amount} {currency}"
    def refund(self, transaction_id: str) -> str: return f"PayPal: возврат {transaction_id}"


class YookassaGateway(Gateway):
    def pay(self, amount: float, currency: str) -> str: return f"ЮKassa: списано {amount} {currency}"
    def refund(self, transaction_id: str) -> str: return f"ЮKassa: возврат {transaction_id}"


class PaymentProcessor(ABC):
    def checkout(self, amount: float, currency: str = "RUB") -> str:
        gateway = self.create_gateway()
        return gateway.pay(amount, currency)


    @abstractmethod
    def create_gateway(self) -> Gateway: ...


class StripeProcessor(PaymentProcessor):
    def create_gateway(self) -> Gateway: return StripeGateway()


class PayPalProcessor(PaymentProcessor):
    def create_gateway(self) -> Gateway: return PayPalGateway()


class YookassaProcessor(PaymentProcessor):
    def create_gateway(self) -> Gateway: return YookassaGateway()


# Пример
if __name__ == "__main__":
    processor = StripeProcessor()
    print(processor.checkout(4990.0))
