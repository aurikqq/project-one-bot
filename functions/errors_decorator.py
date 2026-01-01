import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv
from functools import wraps

load_dotenv()
bot_token = os.getenv('token')

bot = Bot(token = bot_token, default = DefaultBotProperties(parse_mode = 'html'))


def send_errors():
    def decorator(func):
        @wraps(func)
        async def wrapper(message: Message, *args, **kwargs):
            try:
                return await func(message, *args, **kwargs)
            except Exception as e:
                await bot.send_message(1104899353, f"Ошибка при выполнении команды!\n\nКоманда: {message.text}\nИсключение: {e}")
                print(e)

                try:
                    file = FSInputFile("C:\\Users\\Administrator\\Desktop\\bot.log")
                    await bot.send_document(1104899353, file)
                except Exception as error:
                    await bot.send_message(1104899353,f"Не получилось отправить логи.\n\nКонсоль выдала ошибку {error}.")

                await message.reply("Не получилось выполнить команду из-за ошибки. Отчет уже отправлен создателю, от тебя ничего не требуется")
        return wrapper
    return decorator