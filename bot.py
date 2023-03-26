from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from environs import Env


env: Env = Env()
env.read_env()

bot: Bot = Bot(token="6137158393:AAHSresyen2VGkJkGzz7Vf1qpVPvmq--yxM")
dp: Dispatcher = Dispatcher()

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn: KeyboardButton = KeyboardButton(text="Send contact",
                                             request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(text="Send location",
                                         request_location=True)
poll_btn: KeyboardButton = KeyboardButton(text="Create a poll",
                                          request_poll=True)

# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Testing", reply_markup=keyboard)



if __name__ == "__main__":
    dp.run_polling(bot)