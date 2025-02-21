import logging
from aiogram import Bot, Dispatcher, executor, types
from config import Config
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)