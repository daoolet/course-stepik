from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfing:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str
    admin_ids: list


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfing

def load_config(path = None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(
                tg_bot=TgBot(
                    token=env('BOT_TOKEN'),
                    admin_ids=list(map(int, env.list('ADMIN_IDS'))),
                ),
                db=DatabaseConfing(
                    database=env('DATABASE'),
                    db_host=env('DB_HOST'),
                    db_password=env('DB_PASSWORD'),
                    db_user=env('DB_USER')
                ) 
            )