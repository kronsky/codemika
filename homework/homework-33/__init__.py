import telebot
import config
from random import randint

bot = telebot.TeleBot(config.telegram_token)
random_number = 0
attempts = 0


@bot.message_handler(commands=['start'])
def start(message):
    global random_number, attempts
    name = message.from_user.first_name
    random_number = randint(1, 99)
    attempts = 7
    bot.send_message(message.chat.id, 'Привет, ' + name +
                     '!. Я загадал случайное число от 1 до 99. Твоя задача его отгадать. '
                     'Количество попыток: ' + str(attempts))


@bot.message_handler(content_types=['text'])
def text(message):
    global random_number, attempts
    if attempts > 1:
        try:
            message.text = int(message.text)
            if message.text == random_number:
                bot.send_message(message.chat.id, 'Поздравляю, ты угадал')
                start(message)
            else:
                attempts -= 1
                if message.text > random_number:
                    bot.send_message(message.chat.id, 'Меньше. У вас осталось: ' +
                                     str(attempts) + ' попыток')
                else:
                    bot.send_message(message.chat.id, 'Больше. У вас осталось: ' +
                                     str(attempts) + ' попыток')
        except ValueError:
            bot.send_message(message.chat.id, 'Вы ввели не число, попробуйте ещё раз')
    else:
        bot.send_message(message.chat.id, 'Вы проиграли, попытки закончились. '
                                          'Было загадано число: ' + str(random_number))
        start(message)


bot.polling(none_stop=True)
