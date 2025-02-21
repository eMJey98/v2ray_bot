from aiogram import types, Dispatcher
from utils.api import get_user_services, renew_service, add_volume

async def handle_view_services(message: types.Message):
    user_id = message.from_user.id
    services = await get_user_services(user_id)
    await message.answer(f"Your services: {services}")

async def handle_renew_service(message: types.Message):
    user_id = message.from_user.id
    service_id = int(message.get_args())
    await renew_service(user_id, service_id)
    await message.answer("Service renewed successfully!")

async def handle_add_volume(message: types.Message):
    user_id = message.from_user.id
    service_id = int(message.get_args())
    await add_volume(user_id, service_id)
    await message.answer("Volume added successfully!")

def register_service_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_view_services, commands=["view_services"])
    dp.register_message_handler(handle_renew_service, commands=["renew_service"])
    dp.register_message_handler(handle_add_volume, commands=["add_volume"])