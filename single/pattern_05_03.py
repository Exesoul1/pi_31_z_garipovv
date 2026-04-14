import threading


class EventCounter:
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
        if EventCounter._initialized:
            return
        with EventCounter._lock:
            if EventCounter._initialized:
                return
            EventCounter._initialized = True
            self._counts = {}
            self._data_lock = threading.Lock()


    def increment(self, event: str, amount: int = 1) -> None:
        with self._data_lock:
            self._counts[event] = self._counts.get(event, 0) + amount


    def decrement(self, event: str, amount: int = 1) -> None:
        with self._data_lock:
            self._counts[event] = self._counts.get(event, 0) - amount


    def get(self, event: str) -> int:
        with self._data_lock:
            return self._counts.get(event, 0)


    def reset(self, event: str) -> None:
        with self._data_lock:
            self._counts.pop(event, None)


    def all(self) -> dict[str, int]:
        with self._data_lock:
            return dict(self._counts)


if __name__ == "__main__":
    counter = EventCounter()
    counter.increment("login_success")
    counter.increment("login_success")
    counter.increment("login_fail")

    counter2 = EventCounter()
    counter2.increment("api_request", 5)
    counter2.increment("login_success")

    counter3 = EventCounter()
    print(counter3.all())
    assert counter is counter2 is counter3
