from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str: ...


class PdfReport(Report):
    def generate(self, data: dict) -> str:
        return f"[PDF] Отчёт: {data}"


class ExcelReport(Report):
    def generate(self, data: dict) -> str:
        return f"[Excel] Отчёт: {data}"


class CsvReport(Report):
    def generate(self, data: dict) -> str:
        return f"[CSV] Отчёт: {data}"



class ReportManager(ABC):
    def export(self, data: dict) -> str:
        generator = self.create_generator()
        return generator.generate(data)

    @abstractmethod
    def create_generator(self) -> Report: ...


class PdfManager(ReportManager):
    def create_generator(self) -> Report:
        return PdfReport()


class ExcelManager(ReportManager):
    def create_generator(self) -> Report:
        return ExcelReport()


class CsvManager(ReportManager):
    def create_generator(self) -> Report:
        return CsvReport()


# Пример использования
if __name__ == "__main__":
    manager = PdfManager()
    print(manager.export({"title": "Продажи Q1", "total": 150000}))
