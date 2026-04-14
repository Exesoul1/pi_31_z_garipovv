from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float, currency: str) -> str: pass

    @abstractmethod
    def refund(self, transaction_id: str, amount: float) -> str: pass


class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float, currency: str) -> str:
        return f"PayPal: charged {amount} {currency}"

    def refund(self, transaction_id: str, amount: float) -> str:
        return f"PayPal: refunded {amount} for tx {transaction_id}"


class StripeSDK:
    def create_charge(self, amount_cents: int, currency_code: str, metadata: dict) -> dict:
        return {
            "id": "ch_stripe_123",
            "status": "succeeded",
            "amount": amount_cents,
            "currency": currency_code,
        }

    def create_refund(self, charge_id: str, amount_cents: int) -> dict:
        return {"id": "re_stripe_456", "status": "succeeded", "amount": amount_cents}


class StripeAdapter(PaymentProcessor):
    def __init__(self, sdk: StripeSDK):
        self._sdk = sdk

    def pay(self, amount: float, currency: str) -> str:
        self._sdk.create_charge(int(amount * 100), currency, {})
        return f"Stripe: charged {amount} {currency}"

    def refund(self, transaction_id: str, amount: float) -> str:
        self._sdk.create_refund(transaction_id, int(amount * 100))
        return f"Stripe: refunded {amount} for tx {transaction_id}"


def checkout(processor: PaymentProcessor, amount: float, currency: str):
    result = processor.pay(amount, currency)
    print(result)


if __name__ == "__main__":
    checkout(PayPalProcessor(), 1500.0, "RUB")
    checkout(StripeAdapter(StripeSDK()), 1500.0, "RUB")
