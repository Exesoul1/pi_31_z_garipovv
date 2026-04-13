from abc import ABC, abstractmethod


class DbConn(ABC):
    @abstractmethod
    def connect(self) -> None: ...
    @abstractmethod
    def query(self, sql: str) -> list: ...
    @abstractmethod
    def disconnect(self) -> None: ...


class Mysql(DbConn):
    def connect(self) -> None: print("Подключено к MySQL")
    def query(self, sql: str) -> list: print(f"MySQL: {sql}"); return []
    def disconnect(self) -> None: print("Отключено от MySQL")


class Postgres(DbConn):
    def connect(self) -> None: print("Подключено к PostgreSQL")
    def query(self, sql: str) -> list: print(f"PostgreSQL: {sql}"); return []
    def disconnect(self) -> None: print("Отключено от PostgreSQL")


class Sqlite(DbConn):
    def connect(self) -> None: print("Подключено к SQLite")
    def query(self, sql: str) -> list: print(f"SQLite: {sql}"); return []
    def disconnect(self) -> None: print("Отключено от SQLite")


# Базовая фабрика
class DbFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DbConn: ...


# Фабрики для каждой СУБД
class MysqlFactory(DbFactory):
    def create_connection(self) -> DbConn: return Mysql()


class PostgresFactory(DbFactory):
    def create_connection(self) -> DbConn: return Postgres()


class SqliteFactory(DbFactory):
    def create_connection(self) -> DbConn: return Sqlite()


def run_report(factory):
    conn = factory.create_connection()
    conn.connect()
    results = conn.query("SELECT * FROM orders WHERE status = 'new'")
    conn.disconnect()
    return results


if __name__ == "__main__":
    run_report(MysqlFactory())
