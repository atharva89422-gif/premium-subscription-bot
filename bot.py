import telebot

from config import BOT_TOKEN
from handlers import init_bot, show_home

bot = telebot.TeleBot(BOT_TOKEN)

init_bot(bot)


@bot.message_handler(commands=["start"])
def start(message):
    show_home(message)


print("Bot Started...")

bot.infinity_polling(skip_pending=True)
