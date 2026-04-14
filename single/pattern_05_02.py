import threading


class DatabaseConnection:
    _id_counter = 0

    def __init__(self):
        DatabaseConnection._id_counter += 1
        self.id = DatabaseConnection._id_counter
        self.in_use = False

    def execute(self, query: str) -> str:
        return f"[Conn #{self.id}] Результат: {query}"

    def __str__(self) -> str:
        return f"Connection #{self.id}"


class ConnectionPool:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, max_size: int = 5):
        if ConnectionPool._initialized:
            return
        with ConnectionPool._lock:
            if ConnectionPool._initialized:
                return
            ConnectionPool._initialized = True
            self._max_size = max_size
            self._connections: list[DatabaseConnection] = []
            self._available: list[DatabaseConnection] = []
            self._in_use: set[DatabaseConnection] = set()
            self._pool_lock = threading.Lock()

    def acquire(self) -> DatabaseConnection:
        with self._pool_lock:
            if not self._available:
                if len(self._connections) >= self._max_size:
                    raise RuntimeError("Все соединения заняты")
                conn = DatabaseConnection()
                self._connections.append(conn)
                self._available.append(conn)
            conn = self._available.pop()
            conn.in_use = True
            self._in_use.add(conn)
            return conn

    def release(self, conn: DatabaseConnection) -> None:
        with self._pool_lock:
            if conn in self._in_use:
                conn.in_use = False
                self._in_use.remove(conn)
                self._available.append(conn)

    @property
    def active_count(self) -> int:
        with self._pool_lock:
            return len(self._in_use)


if __name__ == "__main__":
    pool = ConnectionPool(max_size=3)
    pool2 = ConnectionPool(max_size=10)
    assert pool is pool2

    conn1 = pool.acquire()
    conn2 = pool.acquire()
    result = conn1.execute("SELECT * FROM users")
    print(result)
    pool.release(conn1)
    print(f"Активных соединений: {pool.active_count}")
