from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, Text

from random import randint

API_TOKEN: str = '6137158393:AAHSresyen2VGkJkGzz7Vf1qpVPvmq--yxM'
ATTEMPTS: int = 5

bot = Bot(API_TOKEN)
dp = Dispatcher()


def get_random_number():
    return randint(1, 100)

user: dict = {
    'in_game': False,
    'secret_number': None,
    'attempts': None,
    'total_games': 0,
    'wins': 0
}


@dp.message(Command(commands=['start']))
async def handler_start_command(message: Message):
    await message.answer("Hello!\nLet's play a game 'Guess the number'\n\n"
                        "To get rules and commands please send /help")


@dp.message(Command(commands=['help']))
async def handler_help_command(message: Message):
    await message.answer(f"Rules:\n\nI will make a secret number (0-100),"
                        f" you have to guess it.\nYou have {ATTEMPTS} attempts.\n\n"
                        f"Available commands: \n/help - rules and commands.\n"
                        f"/cancel - quit.\n/stat - statistics.\n\n"
                        f"Let's play!"
                        )


@dp.message(Command(commands=['stat']))
async def handler_stat_command(message: Message):
    await message.answer(f"Total games played: {user['total_games']}\n"
                        f"Game you won: {user['wins']}")


@dp.message(Command(commands=['cancel']))
async def handler_cancel_command(message: Message):
    if user['in_game']:
        await message.answer("You left the game. If you want to play again just text me :)")
        user['in_game'] = False
    else:
        await message.answer("We do not even playing. May be we should play just one time? :)")


@dp.message(Text(text=['Yes', 'play', 'y', 'game', 'go'], ignore_case=True))
async def handler_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer("I made a secret number (0-100). Go ahead!")
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer("While we are playing the game, I can only respond to a number from 1 to 100 and the commands /cancel and /stat")


@dp.message(Text(text=['no', 'n', 'stop'], ignore_case=True))
async def handler_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer("Sadly :(\n\nIf you want to play just text me")
    else:
        await message.answer("We are already playing. Send me a number (0-100)")


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def handler_numbers_anser(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Hooray!!! You did it!\n\n'
                                 'Again?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Mine number is lower')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Mine number is higher')
            user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(f'Sorry, but you have wasted all your attempts. You lost:(\n\n'
                                 f'Mine secret number was: {user["secret_number"]}\n\n'
                                 f'Lets play one more time')

            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('We are not playing yet. Wanna play?')


@dp.message()
async def handler_other_text_answers(message: Message):
    if user['in_game']:
        await message.answer("We are already playing. Just send me a number (0-100)")
    else:
        await message.answer("I'm a pretty limited bot, let's just play a game?")

if __name__ == '__main__':
    dp.run_polling(bot)