import telebot

from config import BOT_TOKEN
from handlers import (
    init_bot,
    show_home,
    show_plans,
    show_payment
)

bot = telebot.TeleBot(BOT_TOKEN)

init_bot(bot)


@bot.message_handler(commands=["start"])
def start(message):
    show_home(message)


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    if call.data == "premium":
        show_plans(call.message.chat.id)

    elif call.data == "plan_7_days":
        show_payment(call.message.chat.id, "7_days")

    elif call.data == "plan_15_days":
        show_payment(call.message.chat.id, "15_days")

    elif call.data == "plan_30_days":
        show_payment(call.message.chat.id, "30_days")

    elif call.data == "plan_1_year":
        show_payment(call.message.chat.id, "1_year")

    bot.answer_callback_query(call.id)


print("Bot Started...")

bot.infinity_polling(skip_pending=True)
