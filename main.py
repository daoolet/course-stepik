from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command


BOT_TOKEN: str = '6137158393:AAHSresyen2VGkJkGzz7Vf1qpVPvmq--yxM'

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=["start"]))
async def procces_start_command(message: Message):
    await message.answer("Hello, \nI am Echo-bot! \nText me")

@dp.message(Command(commands=["help"]))
async def procces_help_command(message: Message):
    await message.answer("Text me something and I will reply your message")


@dp.message()
async def send_echo(message: Message):
    try:
        print(message.json())
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')
                                 
'''

# async def send_photo_echo(message: Message):
#     await message.reply_photo(message.photo[0].file_id)

# async def send_sticker_echo(message: Message):
#     print(message.json())
#     await message.reply_sticker(message.sticker.file_id)
    
# async def send_audio_echo(message: Message):
#     print(message.json())
#     await message.reply_audio(message.aud)
    
# async def send_video_echo(message: Message):
#     print(message.json())
#     await message.reply_video(message.photo[0].file_id)
    
# async def send_voice_echo(message: Message):
#     print(message.json())
#     await message.reply_voice()

# dp.message.register(send_sticker_echo, F.sticker)
# dp.message.register(send_photo_echo, F.photo)

# dp.message.register(send_audio_echo, F.audio)
# dp.message.register(send_video_echo, F.video)
# dp.message.register(send_voice_echo, F.voice)

# dp.message.register(send_animation_echo, F.animation)
# dp.message.register(send_document_echo, F.document)

# dp.message.register(send_echo)
'''

if __name__ == '__main__':
    dp.run_polling(bot)