from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    user: str
    password: str
    host: str
    port: int
    database: str

db_config = DatabaseConfig(
    user='root',
    password='your-database-password',
    host='localhost',
    port=3306,
    database='your-created-mysql-database'
)
