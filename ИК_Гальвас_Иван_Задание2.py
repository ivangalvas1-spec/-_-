import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI"])

import random
import telebot

TOKEN = "8868830557:AAHEWDD1VnruAoAsvf34GVzc89RGpa_fwm8"
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
    line = random.choice(LINES)
    bot.send_message(message.chat.id, line)


print("Бот запущен")
bot.infinity_polling()
