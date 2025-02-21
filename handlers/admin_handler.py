from aiogram import types, Dispatcher
from config import Config

async def handle_admin(message: types.Message):
    if message.from_user.id == Config.ADMIN_ID:
        await message.answer("Welcome, admin! You can manage the bot here.")
    else:
        await message.answer("You are not authorized to use this command.")

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_admin, commands=["admin"])