class SelectQueryBuilder:
    def __init__(self):
        self._table = ""
        self._columns = []
        self._wheres = []
        self._joins = []
        self._order = None
        self._limit_val = None
        self._offset_val = None


    def from_table(self, table: str):
        self._table = table
        return self


    def select(self, *columns: str):
        self._columns = list(columns)
        return self


    def where(self, condition: str):
        self._wheres.append(condition)
        return self


    def join(self, table: str, on: str):
        self._joins.append(f"JOIN {table} ON {on}")
        return self


    def order_by(self, column: str, direction: str = "ASC"):
        self._order = f"{column} {direction.upper()}"
        return self


    def limit(self, value: int):
        self._limit_val = value
        return self


    def offset(self, value: int):
        self._offset_val = value
        return self


    def build(self) -> str:
        cols = ", ".join(self._columns) if self._columns else "*"
        sql = f"SELECT {cols}\nFROM {self._table}"

        for join in self._joins:
            sql += f"\n{join}"

        if self._wheres:
            sql += "\nWHERE " + " AND ".join(self._wheres)

        if self._order:
            sql += f"\nORDER BY {self._order}"

        if self._limit_val is not None:
            sql += f"\nLIMIT {self._limit_val}"

        if self._offset_val is not None:
            sql += f" OFFSET {self._offset_val}"

        return sql


if __name__ == "__main__":
    sql = (
        SelectQueryBuilder()
        .from_table("orders")
        .select("id", "total", "status")
        .join("users", "orders.user_id = users.id")
        .where("status = 'new'")
        .where("total > 1000")
        .order_by("created_at", "DESC")
        .limit(10)
        .offset(20)
        .build()
    )
    print(sql)
    print("-" * 40)

    sql_min = SelectQueryBuilder().from_table("products").build()
    print(sql_min)
