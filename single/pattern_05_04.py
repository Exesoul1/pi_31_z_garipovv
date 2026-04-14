import time
import threading


class MemoryCache:
    _instance = None
    _lock = threading.Lock()
    _initialized = False


    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if MemoryCache._initialized:
            return
        with MemoryCache._lock:
            if MemoryCache._initialized:
                return
            MemoryCache._initialized = True
            self._store = {}
            self._data_lock = threading.Lock()


    def set(self, key: str, value, ttl: float = 60.0) -> None:
        with self._data_lock:
            self._store[key] = (value, time.time() + ttl)


    def get(self, key: str):
        with self._data_lock:
            if key in self._store:
                value, expire_at = self._store[key]
                if time.time() < expire_at:
                    return value
                del self._store[key]
            return None


    def delete(self, key: str) -> None:
        with self._data_lock:
            self._store.pop(key, None)


    def flush(self) -> None:
        with self._data_lock:
            self._store.clear()


    @property
    def size(self) -> int:
        with self._data_lock:
            now = time.time()
            live_keys = [k for k, (_, exp) in self._store.items() if now < exp]
            for k in list(self._store.keys()):
                if k not in live_keys:
                    del self._store[k]
            return len(live_keys)


if __name__ == "__main__":
    cache = MemoryCache()
    cache2 = MemoryCache()
    assert cache is cache2

    cache.set("user:1", {"name": "Анна", "role": "admin"}, ttl=2.0)
    cache.set("user:2", {"name": "Иван", "role": "user"}, ttl=60.0)

    print(cache.get("user:1"))
    print(cache2.get("user:2"))

    time.sleep(2.1)
    print(cache.get("user:1"))
    print(cache.size)
