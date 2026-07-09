from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["premium_subscription_bot"]

users_col = db["users"]
payments_col = db["payments"]
channels_col = db["channels"]


def add_user(user_id, username, first_name):
    users_col.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "username": username,
                "first_name": first_name
            }
        },
        upsert=True
    )


def get_user(user_id):
    return users_col.find_one({"user_id": user_id})
