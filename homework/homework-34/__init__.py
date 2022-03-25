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
    city_id = weather.get_city_id(city, language)
    if type(city_id) == int:
        desc, temp, city = weather.get(city_id, language)
        mess = f'Погода в городе {city}\nТемпература: {temp} °C\n{desc}'
        bot.send_message(message.chat.id, mess)
    else:
        bot.send_message(message.chat.id, 'Город не найден')


bot.polling(none_stop=True)
