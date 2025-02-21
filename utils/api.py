import requests
from config import Config

async def create_vpn_config(user_id):
    response = requests.post(
        f"{Config.V2RAY_PANEL_URL}/api/v1/config/create",
        headers={"Authorization": f"Bearer {Config.V2RAY_PANEL_API_KEY}"},
        json={"user_id": user_id}
    )
    if response.status_code == 200:
        return response.json()["config"]
    else:
        return None

async def get_user_services(user_id):
    response = requests.get(
        f"{Config.V2RAY_PANEL_URL}/api/v1/user/{user_id}/services",
        headers={"Authorization": f"Bearer {Config.V2RAY_PANEL_API_KEY}"}
    )
    if response.status_code == 200:
        return response.json()["services"]
    else:
        return None

async def renew_service(user_id, service_id):
    response = requests.post(
        f"{Config.V2RAY_PANEL_URL}/api/v1/service/{service_id}/renew",
        headers={"Authorization": f"Bearer {Config.V2RAY_PANEL_API_KEY}"},
        json={"user_id": user_id}
    )
    return response.status_code == 200

async def add_volume(user_id, service_id):
    response = requests.post(
        f"{Config.V2RAY_PANEL_URL}/api/v1/service/{service_id}/add_volume",
        headers={"Authorization": f"Bearer {Config.V2RAY_PANEL_API_KEY}"},
        json={"user_id": user_id}
    )
    return response.status_code == 200