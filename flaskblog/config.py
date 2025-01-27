
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    print(os.getenv("DATABASE_URI"))
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("EMAIL_ADDRESS")
    MAIL_PASSWORD = os.getenv("PASSWORD")
