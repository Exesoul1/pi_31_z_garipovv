from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def connect(self, dsn: str) -> None: pass
    @abstractmethod
    def close(self) -> None: pass


class QueryBuilder(ABC):
    @abstractmethod
    def select(self, table: str, columns: list[str]) -> str: pass
    @abstractmethod
    def where(self, condition: str) -> str: pass


class Transaction(ABC):
    @abstractmethod
    def begin(self) -> None: pass
    @abstractmethod
    def commit(self) -> None: pass
    @abstractmethod
    def rollback(self) -> None: pass


# MySQL 
class MysqlConn(Connection):
    def connect(self, dsn: str) -> None: print(f"MySQL: connect → {dsn}")
    def close(self) -> None: print("MySQL: close")


class MysqlQuery(QueryBuilder):
    def select(self, table: str, columns: list[str]) -> str: return f"SELECT {', '.join(columns)} FROM {table}"
    def where(self, condition: str) -> str: return f"WHERE {condition}"


class MysqlTx(Transaction):
    def begin(self) -> None: print("MySQL: BEGIN")
    def commit(self) -> None: print("MySQL: COMMIT")
    def rollback(self) -> None: print("MySQL: ROLLBACK")


# PostgreSQL 
class PgConn(Connection):
    def connect(self, dsn: str) -> None: print(f"PostgreSQL: connect → {dsn}")
    def close(self) -> None: print("PostgreSQL: close")


class PgQuery(QueryBuilder):
    def select(self, table: str, columns: list[str]) -> str: return f"SELECT {', '.join(columns)} FROM {table}"
    def where(self, condition: str) -> str: return f"WHERE {condition}"


class PgTx(Transaction):
    def begin(self) -> None: print("PostgreSQL: BEGIN")
    def commit(self) -> None: print("PostgreSQL: COMMIT")
    def rollback(self) -> None: print("PostgreSQL: ROLLBACK")


# Абстрактная фабрика
class DbFactory(ABC):
    @abstractmethod
    def create_connection(self) -> Connection: ...
    @abstractmethod
    def create_query_builder(self) -> QueryBuilder: ...
    @abstractmethod
    def create_transaction(self) -> Transaction: ...


class MysqlFactory(DbFactory):
    def create_connection(self) -> Connection: return MysqlConn()
    def create_query_builder(self) -> QueryBuilder: return MysqlQuery()
    def create_transaction(self) -> Transaction: return MysqlTx()


class PgFactory(DbFactory):
    def create_connection(self) -> Connection: return PgConn()
    def create_query_builder(self) -> QueryBuilder: return PgQuery()
    def create_transaction(self) -> Transaction: return PgTx()


def run_query(factory: DbFactory):
    conn = factory.create_connection()
    qb = factory.create_query_builder()
    tx = factory.create_transaction()

    conn.connect("host=localhost dbname=shop")
    tx.begin()
    sql = qb.select("orders", ["id", "total"]) + " " + qb.where("status = 'new'")
    print(f"Запрос: {sql}")
    tx.commit()
    conn.close()


if __name__ == "__main__":
    run_query(MysqlFactory())
    print("-" * 20)
    run_query(PgFactory())
