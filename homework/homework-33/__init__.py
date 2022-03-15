import telebot
import config

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, 'Привет, чумба!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Справка находится в разработке...')


@bot.message_handler(content_types=['text'])
def text(message):
    print(message)
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Я же уже поздоровался :)')
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю...')


bot.polling(none_stop=True)


