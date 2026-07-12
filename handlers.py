import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import PLANS, UPI_ID
from database import add_user

bot = None


def init_bot(bot_instance):
    global bot
    bot = bot_instance


def show_home(message):
    add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    )

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "💎 Premium Content",
            callback_data="premium"
        )
    )

    bot.send_message(
        message.chat.id,
        "👋 Welcome!\n\nChoose an option below.",
        reply_markup=markup
    )


def show_plans(chat_id):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            f"💎 7 Days - ₹{PLANS['7_days']['price']}",
            callback_data="plan_7_days"
        )
    )

    markup.add(
        InlineKeyboardButton(
            f"💎 30 Days - ₹{PLANS['30_days']['price']}",
            callback_data="plan_30_days"
        )
    )

    bot.send_message(
        chat_id,
        "📦 Select your subscription plan:",
        reply_markup=markup
    )
def show_payment(chat_id, plan):
    data = PLANS[plan]

    text = f"""
💎 Premium Subscription

📦 Plan : {data['name']}
💰 Price : ₹{data['price']}

💳 UPI ID:
`{UPI_ID}`

✅ Payment karne ke baad payment screenshot yahi bhej dijiye.

Admin verify karne ke baad aapko automatic Premium access mil jayega.
"""

    bot.send_message(
        chat_id,
        text,
        parse_mode="Markdown"
    )
