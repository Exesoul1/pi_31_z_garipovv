from abc import ABC, abstractmethod


class Header(ABC):
    @abstractmethod
    def render(self, title: str, subtitle: str) -> str: pass


class Table(ABC):
    @abstractmethod
    def render(self, headers: list[str], rows: list[list]) -> str: pass


class Footer(ABC):
    @abstractmethod
    def render(self, text: str, page: int) -> str: pass


# PDF-компоненты
class PdfHeader(Header):
    def render(self, title: str, subtitle: str) -> str: return f"[PDF] Заголовок: {title} | {subtitle}\n"


class PdfTable(Table):
    def render(self, headers: list[str], rows: list[list]) -> str: return f"[PDF] Таблица: {headers}\n"


class PdfFooter(Footer):
    def render(self, text: str, page: int) -> str: return f"[PDF] Подвал: {text} (стр. {page})\n"


# DOCX-компоненты
class DocxHeader(Header):
    def render(self, title: str, subtitle: str) -> str: return f"[DOCX] Заголовок: {title} - {subtitle}\n"


class DocxTable(Table):
    def render(self, headers: list[str], rows: list[list]) -> str: return f"[DOCX] Таблица: {headers}\n"


class DocxFooter(Footer):
    def render(self, text: str, page: int) -> str: return f"[DOCX] Подвал: {text} - стр. {page}\n"


# Абстрактная фабрика
class DocumentFactory(ABC):
    @abstractmethod
    def create_header(self) -> Header: pass
    @abstractmethod
    def create_table(self) -> Table: pass
    @abstractmethod
    def create_footer(self) -> Footer: pass


class PdfFactory(DocumentFactory):
    def create_header(self) -> Header: return PdfHeader()
    def create_table(self) -> Table: return PdfTable()
    def create_footer(self) -> Footer: return PdfFooter()


class DocxFactory(DocumentFactory):
    def create_header(self) -> Header: return DocxHeader()
    def create_table(self) -> Table: return DocxTable()
    def create_footer(self) -> Footer: return DocxFooter()


def build_sales_report(factory: DocumentFactory, data: list[list]) -> str:
    header = factory.create_header()
    table  = factory.create_table()
    footer = factory.create_footer()

    result  = header.render("Отчёт о продажах", "Квартал 1, 2025")
    result += table.render(["Продукт", "Количество", "Сумма"], data)
    result += footer.render("Конфиденциально", 1)
    return result


if __name__ == "__main__":
    sales_data = [["Ноутбук", 5, 500000], ["Мышь", 20, 10000]]
    
    print(build_sales_report(PdfFactory(), sales_data))
    print(build_sales_report(DocxFactory(), sales_data))
