from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU


# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU["no_button"])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# # Добавляем кнопки в билдер с параметром width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU["rock"])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU["paper"])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU["scissors"])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1],
                                              [button_2],
                                              [button_3]],
                                    resize_keyboard=True)