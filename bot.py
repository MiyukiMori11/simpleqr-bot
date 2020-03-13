import telebot
import config
from qrgenerator import generate
import os


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_msg(msg):
    bot.send_message(msg.chat.id, 'Hello! Send me any text to get a Qr code')


@bot.message_handler(content_types=['text'])
def get_txt(msg):
    txt = msg.text
    file = generate(txt)
    with open(file, 'rb') as send:
        bot.send_photo(msg.chat.id, send)
    os.remove(file)


bot.polling()
