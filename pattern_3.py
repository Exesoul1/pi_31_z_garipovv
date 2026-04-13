from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def parse(self, raw: str) -> list[dict]:
        pass


class JsonParser(Parser):
    def parse(self, raw: str) -> list[dict]:
        import json
        return json.loads(raw)


class CsvParser(Parser):
    def parse(self, raw: str) -> list[dict]:
        import csv, io
        return list(csv.DictReader(io.StringIO(raw)))


class XmlParser(Parser):
    def parse(self, raw: str) -> list[dict]:
        import xml.etree.ElementTree as ET
        root = ET.fromstring(raw)
        return [{child.tag: child.text for child in item} for item in root]


# Абстрактный создатель
class DataImporter(ABC):

    def parse(self, raw: str) -> list[dict]:
        parser = self.create_parser()
        return parser.parse(raw)

   
    @abstractmethod
    def create_parser(self) -> Parser:
        pass


class JsonImporter(DataImporter):
    def create_parser(self) -> Parser:
        return JsonParser()


class CsvImporter(DataImporter):
    def create_parser(self) -> Parser:
        return CsvParser()


class XmlImporter(DataImporter):
    def create_parser(self) -> Parser:
        return XmlParser()


# Пример использования
if __name__ == "__main__":
    raw_json = '[{"id": 1, "name": "Test"}]'
    
    importer = JsonImporter()
    print(importer.parse(raw_json))
