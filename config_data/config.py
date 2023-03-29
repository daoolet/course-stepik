from dataclasses import dataclass

from environs import Env

@dataclass
class Tgbot:
    token: str

@dataclass
class Config:
    tg_bot: Tgbot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env()
    return Config(tg_bot=Tgbot(token=env("BOT_TOKEN")))