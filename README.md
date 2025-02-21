# V2Ray Bot

A Telegram bot for managing V2Ray VPN services, integrated with Alireza0 X-UI V2Ray panel.

## Features

- VPN Purchase with Auto Configuration Creation
- View Purchased Services
- Trial Accounts for Users
- User Support Section
- Verification via Phone Number
- Payments via PayPal
- Fully Automated Configuration Creation
- Compatibility with All Protocols
- Mandatory Channel Membership for Purchases
- Detailed Purchase and Trial Account Reports
- Tutorial Section with Admin-Customizable Content
- Balance Management via Admin Panel
- Multiple Admin Support
- Manage Purchased Services:
  - Renewals
  - Additional Volume Purchases
  - Configuration Retrieval
  - Updating Service Links
- FAQ Section
- Text Customization from the Bot
- Product and Panel Management
- Admin-Specified Username Generation Methods
- Configuration Settings Based on Protocols
- Gateway Management

## Installation

### Prerequisites

- Ubuntu Server 22
- A Domain Name

### Installing the Bot

Run the following command in your server terminal:

```bash
git clone https://github.com/your-repo/v2ray_bot.git
cd v2ray_bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set up environment variables:

```bash
export TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
export ADMIN_ID="your_admin_id"
export DATABASE_URL="your_database_url"
export V2RAY_PANEL_URL="your_v2ray_panel_url"
export V2RAY_PANEL_API_KEY="your_v2ray_panel_api_key"
export PAYPAL_CLIENT_ID="your_paypal_client_id"
export PAYPAL_CLIENT_SECRET="your_paypal_client_secret"
```

Run the bot:

```bash
python bot.py
```

## Usage

Interact with the bot using Telegram commands:

- `/purchase` - Purchase VPN service
- `/view_services` - View purchased services
- `/renew_service <service_id>` - Renew a service
- `/add_volume <service_id>` - Add volume to a service
- `/support` - Contact support
- `/admin` - Admin panel