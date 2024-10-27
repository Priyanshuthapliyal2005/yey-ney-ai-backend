# config.py
from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
