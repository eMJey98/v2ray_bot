import requests
from config import Config

async def process_paypal_payment(user_id, amount):
    paypal_auth = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        auth=(Config.PAYPAL_CLIENT_ID, Config.PAYPAL_CLIENT_SECRET),
        headers={"Accept": "application/json", "Accept-Language": "en_US"},
        data={"grant_type": "client_credentials"}
    )
    access_token = paypal_auth.json().get("access_token")
    if access_token:
        payment_response = requests.post(
            "https://api-m.sandbox.paypal.com/v1/payments/payment",
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"},
            json={
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "transactions": [{
                    "amount": {"total": str(amount), "currency": "USD"},
                    "description": f"VPN Service Purchase for user {user_id}"
                }],
                "redirect_urls": {
                    "return_url": "https://yourdomain.com/paypal_success",
                    "cancel_url": "https://yourdomain.com/paypal_cancel"
                }
            }
        )
        return payment_response.status_code == 201
    return False