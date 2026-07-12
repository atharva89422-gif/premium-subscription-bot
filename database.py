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
from datetime import datetime, timedelta


def save_payment(user_id, plan_name, amount, screenshot_file_id):
    payments_col.insert_one({
        "user_id": user_id,
        "plan": plan_name,
        "amount": amount,
        "screenshot": screenshot_file_id,
        "status": "pending",
        "created_at": datetime.utcnow()
    })


def get_pending_payments():
    return list(payments_col.find({"status": "pending"}))


def approve_payment(user_id, days):
    expiry = datetime.utcnow() + timedelta(days=days)

    users_col.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "premium": True,
                "expiry": expiry
            }
        },
        upsert=True
    )

    payments_col.update_one(
        {
            "user_id": user_id,
            "status": "pending"
        },
        {
            "$set": {
                "status": "approved"
            }
        }
    )

def reject_payment(user_id):
    payments_col.update_one(
        {
            "user_id": user_id,
            "status": "pending"
        },
        {
            "$set": {
                "status": "rejected"
            }
        }
    )


def get_active_users():
    return list(users_col.find({"premium": True}))



def get_expired_users():
    return list(
        users_col.find(
            {
                "premium": True,
                "expiry": {
                    "$lte": datetime.utcnow()
                }
            }
        )
    )


def remove_premium(user_id):
    users_col.update_one(
        {
            "user_id": user_id
        },
        {
            "$set": {
                "premium": False
            }
        }
    )


def total_active():
    return users_col.count_documents(
        {
            "premium": True
        }
    )
