from aiogram import types, Dispatcher

async def handle_support(message: types.Message):
    await message.answer("Please describe your issue. Our support team will contact you shortly.")

def register_support_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_support, commands=["support"])