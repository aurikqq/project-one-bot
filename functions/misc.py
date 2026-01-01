import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('token')

bot = Bot(token = bot_token, default = DefaultBotProperties(parse_mode = 'html'))


async def get_bot_logs(message: Message):
    if message.from_user.id not in [6668023008, 5433731633, 1104899353]:
        await message.reply("Логи бота может получить только Айрик - тебе они ни к чему.")
    else:
        if message.chat.type != "private":
            await message.reply("Отправил логи в ЛС!")
        try:
            file = FSInputFile(path = "C:\\Users\\Administrator\\Desktop\\bot.log")
            await bot.send_document(1104899353, file)
        except Exception as error:
            await bot.send_message(1104899353, f"Не получилось отправить логи.\n\nКонсоль выдала ошибку:\n\n{error}.")