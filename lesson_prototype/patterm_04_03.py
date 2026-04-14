import copy
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    host: str
    port: int
    name: str
    pool_size: int


class ServerConfig:
    def __init__(
        self,
        host: str,
        port: int,
        debug: bool,
        db: DatabaseConfig,
        allowed_hosts: list[str],
        env_vars: dict[str, str],
    ):
        self.host = host
        self.port = port
        self.debug = debug
        self.db = db
        self.allowed_hosts = allowed_hosts
        self.env_vars = env_vars


    def __str__(self) -> str:
        return (
            f"Server {self.host}:{self.port} debug={self.debug}\n"
            f"  DB: {self.db.host}:{self.db.port}/{self.db.name} pool={self.db.pool_size}\n"
            f"  Hosts: {self.allowed_hosts}\n"
            f"  Env: {self.env_vars}"
        )


    def clone(self) -> "ServerConfig":
        return copy.deepcopy(self)



base = ServerConfig(
    host="0.0.0.0", port=8000, debug=False,
    db=DatabaseConfig("db.internal", 5432, "app_db", pool_size=5),
    allowed_hosts=["localhost"],
    env_vars={"TZ": "UTC"},
)


if __name__ == "__main__":
    dev = base.clone()
    dev.debug = True
    dev.db.name = "app_db_dev"
    dev.allowed_hosts.append("dev.example.com")
    dev.env_vars["DEBUG_SQL"] = "1"

    prod = base.clone()
    prod.port = 443
    prod.db.pool_size = 20

    print("=== BASE ===")
    print(base)
    print("\n=== DEV ===")
    print(dev)
    print("\n=== PROD ===")
    print(prod)
