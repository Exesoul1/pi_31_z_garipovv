import json
import os
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Dict, Any

# ──────────────────────────────────────────────────────────────
# 1. МОДЕЛИ
# ──────────────────────────────────────────────────────────────
@dataclass
class Order:
    id: str
    price: float
    qty: int
    customer_email: str

@dataclass
class ReportMetrics:
    count: int
    total: float

# ──────────────────────────────────────────────────────────────
# 2. КОМПОНЕНТЫ
# ──────────────────────────────────────────────────────────────
class JsonLoader:
    def load(self, path: str) -> List[Dict[str, Any]]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

class OrderParser:
    def parse(self, raw: List[Dict[str, Any]]) -> List[Order]:
        required = {"id", "price", "qty", "email"}
        orders = []
        for item in raw:
            if not required.issubset(item.keys()):
                raise ValueError("Invalid order payload")
            if item["qty"] <= 0:
                raise ValueError("qty must be positive")
            orders.append(Order(
                id=str(item["id"]), price=float(item["price"]),
                qty=int(item["qty"]), customer_email=str(item["email"])
            ))
        return orders

class OrderCalculator:
    def calculate(self, orders: List[Order]) -> ReportMetrics:
        total = sum(o.price * o.qty for o in orders)
        return ReportMetrics(count=len(orders), total=total)

class ReportFormatter:
    def format(self, metrics: ReportMetrics) -> str:
        return f"Orders count: {metrics.count}\nTotal: {metrics.total:.2f}\n"

class ReportSender(ABC):
    @abstractmethod
    def send(self, orders: List[Order], report_text: str) -> None: ...

class EmailSender(ReportSender):
    def send(self, orders: List[Order], report_text: str) -> None:
        for o in orders:
            print(f"[EMAIL to={o.customer_email}] Your order report\n{report_text}")

class NoOpSender(ReportSender):
    def send(self, orders: List[Order], report_text: str) -> None:
        pass

# ──────────────────────────────────────────────────────────────
# 3. ОРКЕСТРАТОР
# ──────────────────────────────────────────────────────────────
class OrderReportService:
    def __init__(self, loader, parser, calculator, formatter, sender):
        self.loader = loader
        self.parser = parser
        self.calculator = calculator
        self.formatter = formatter
        self.sender = sender

    def make_and_send_report(self, json_path: str) -> str:
        raw = self.loader.load(json_path)
        orders = self.parser.parse(raw)
        metrics = self.calculator.calculate(orders)
        report = self.formatter.format(metrics)
        self.sender.send(orders, report)
        return report

# ──────────────────────────────────────────────────────────────
# 4. ТОЧКА ВХОДА
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    JSON_PATH = "orders.json"

    #  Автогенерация тестовых данных (если файла нет)
    if not os.path.exists(JSON_PATH):
        sample = [
            {"id": "ORD-1", "price": 150.0, "qty": 2, "email": "alice@example.com"},
            {"id": "ORD-2", "price": 45.5, "qty": 10, "email": "bob@example.com"}
        ]
        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(sample, f, ensure_ascii=False, indent=2)
        print(f" Создан тестовый файл: {JSON_PATH}\n")

    #  Сборка сервиса (здесь можно легко менять компоненты)
    service = OrderReportService(
        loader=JsonLoader(),
        parser=OrderParser(),
        calculator=OrderCalculator(),
        formatter=ReportFormatter(),
        sender=EmailSender()  # ← замените на NoOpSender(), чтобы отключить рассылку
    )

    #  Запуск
    try:
        print(" Генерация отчёта...")
        report = service.make_and_send_report(JSON_PATH)
        print("\n Итоговый отчёт:")
        print(report)
    except Exception as e:
        print(f"\n Ошибка выполнения: {e}")
