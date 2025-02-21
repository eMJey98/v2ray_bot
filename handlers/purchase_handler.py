from aiogram import types, Dispatcher
from utils.api import create_vpn_config
from utils.payment import process_paypal_payment

async def handle_purchase(message: types.Message):
    user_id = message.from_user.id
    amount = 10  # Example amount, you can customize it as needed
    
    # Process PayPal payment
    payment_status = await process_paypal_payment(user_id, amount)
    if payment_status:
        # Create VPN config
        vpn_config = await create_vpn_config(user_id)
        await message.answer(f"Your VPN configuration: {vpn_config}")
    else:
        await message.answer("Payment failed. Please try again.")

def register_purchase_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_purchase, commands=["purchase"])