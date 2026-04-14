import threading


class FeatureFlagManager:
    _instance = None
    _lock = threading.Lock()
    _initialized = False


    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._flags = {}
        return cls._instance


    def initialize(self, flags: dict[str, bool]) -> None:
        with FeatureFlagManager._lock:
            if FeatureFlagManager._initialized:
                return
            self._flags = dict(flags)
            FeatureFlagManager._initialized = True


    def is_enabled(self, flag: str) -> bool:
        if flag not in self._flags:
            raise KeyError(flag)
        return self._flags[flag]


    def enable(self, flag: str) -> None:
        if flag not in self._flags:
            raise KeyError(flag)
        self._flags[flag] = True


    def disable(self, flag: str) -> None:
        if flag not in self._flags:
            raise KeyError(flag)
        self._flags[flag] = False


    def get_all(self) -> dict[str, bool]:
        return dict(self._flags)


if __name__ == "__main__":
    flags = FeatureFlagManager()
    flags.initialize({
        "new_checkout": False,
        "dark_mode": True,
        "ai_recommendations": False,
        "beta_api": False,
    })

    fm = FeatureFlagManager()
    if fm.is_enabled("dark_mode"):
        print("Тёмная тема активна")

    fm2 = FeatureFlagManager()
    fm2.enable("new_checkout")
    print(fm.is_enabled("new_checkout"))

    try:
        fm.is_enabled("unknown_feature")
    except KeyError as e:
        print(f"Ошибка: {e}")
