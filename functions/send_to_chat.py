import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message

from dotenv import load_dotenv


load_dotenv()
bot_token = os.getenv('token')
chat_id = os.getenv('chat_id')

bot = Bot(token = bot_token, default = DefaultBotProperties(parse_mode = 'html'))


async def send_message_to_chat(message: Message):
    if message.from_user.id in [6668023008, 5433731633, 1104899353]:
        text = message.text.replace("/send_msg ", '')
        await bot.send_message(chat_id, text)
    else:
        await message.reply("Это не для тебя!")