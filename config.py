import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "PASTE_YOUR_BOT_TOKEN")

ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority"
)

UPI_ID = os.getenv("UPI_ID", "yourupi@upi")

CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001234567890"))

CHANNEL_NAME = "Premium Channel"

PLANS = {
    "7_days": {
        "name": "7 Days",
        "price": 69,
        "days": 7
    },

    "15_days": {
        "name": "15 Days",
        "price": 110,
        "days": 15
    },

    "30_days": {
        "name": "30 Days",
        "price": 199,
        "days": 30
    },

    "1_year": {
        "name": "1 Year",
        "price": 499,
        "days": 365
    }
}
