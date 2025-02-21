from utils.database import engine, Base
from models.user import User
from models.service import Service
from models.payment import Payment

# Create all tables in the database
Base.metadata.create_all(bind=engine)

print("Database initialized!")