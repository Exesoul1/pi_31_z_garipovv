class AppConfig:
    _instance = None
    _initialized = False


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if AppConfig._initialized:
            return
        AppConfig._initialized = True
        self.settings = {}


    @classmethod
    def init(cls, settings: dict):
        if not cls._initialized:
            instance = cls()
            instance.settings = settings


    def get(self, key: str, default=None):
        return self.settings.get(key, default)


    def set(self, key: str, value) -> None:
        self.settings[key] = value


if __name__ == "__main__":
    AppConfig.init({"debug": False, "db_host": "localhost", "db_port": 5432})

    config_a = AppConfig()
    config_b = AppConfig()

    config_a.set("debug", True)

    print(config_b.get("debug")) 
    print(config_a is config_b) 
