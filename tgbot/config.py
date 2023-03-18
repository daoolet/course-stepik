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


env = Env()
env.read_env()

config = Config(
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


# print('BOT_TOKEN:', config.tg_bot.token)
# print('ADMIN_IDS:', config.tg_bot.admin_ids)
# print()
# print('DATABASE:', config.db.database)
# print('DB_HOST:', config.db.db_host)
# print('DB_USER:', config.db.db_user)
# print('DB_PASSWORD:', config.db.db_password)