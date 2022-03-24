import telebot
import config
import openweather as weather

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = 'Привет! Это бот для определения погоды по названию города'
    bot.send_message(message.chat.id, welcome_message)


@bot.message_handler(content_types=['text'])
def text(message):
    language = message.from_user.language_code
    city = message.text
    desc, temp, city = weather.get(city, language)
    mess = f'Погода в городе {city}\nТемпература: {temp} °C\n{desc}'
    bot.send_message(message.chat.id, mess)


bot.polling(none_stop=True)
