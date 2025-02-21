from .purchase_handler import register_purchase_handlers
from .service_handler import register_service_handlers
from .support_handler import register_support_handlers
from .admin_handler import register_admin_handlers

def register_handlers(dp):
    register_purchase_handlers(dp)
    register_service_handlers(dp)
    register_support_handlers(dp)
    register_admin_handlers(dp)