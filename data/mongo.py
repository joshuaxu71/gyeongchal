import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

connection_string = os.getenv("MONGO_URI")
client = MongoClient(connection_string)
db = client['gyeongchal']