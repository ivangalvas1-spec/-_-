import os
import random
import telebot

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise SystemExit("Не задана переменная окружения BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

LINES = [
    "Если прощу тебя сейчас, то не прощу себя потом",
    "Первый миллион, Я первый чемпион",
    "В уродстве вижу красоту",
]


@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "Йоу! 👋 Я бот по треку «ДИНАСТИЯ» от madk1d.\n\n"
        "Что я умею:\n"
        "/start — показать это сообщение\n"
        "/swaga — кинуть случайную строчку из трека 🔥"
    )
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["swaga"])
def swaga(message):
    bot.send_message(message.chat.id, random.choice(LINES))


print("Бот запущен")
bot.infinity_polling()

#   
