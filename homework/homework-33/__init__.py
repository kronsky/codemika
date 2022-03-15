import telebot
import config
from random import randint

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    name = message.from_user.first_name
    bot.send_message(message.chat.id, 'Привет, ' + name + '!')
    bot.send_message(message.chat.id, 'Я загадал случайное число, твоя задача его отгадать')


@bot.message_handler(content_types=['text'])
def text(message):
    print(message)
    try:
        message.text = int(message.text)
        bot.send_message(message.chat.id, 'OK')
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели не число, попробуйте ещё раз')


bot.polling(none_stop=True)
