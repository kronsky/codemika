import telebot
import config
import openweather as weather
from telebot import types

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = 'Привет! Это бот для определения погоды в твоей локации.'
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_item_location = types.KeyboardButton('Узнать погоду', request_location=True)
    menu.add(menu_item_location)
    bot.send_message(message.chat.id, welcome_message, reply_markup=menu)


@bot.message_handler(content_types=['location'])
def get_weather(message):
    language = message.from_user.language_code
    latitude = message.location.latitude
    longitude = message.location.longitude
    desc, temp, city = weather.get(longitude, latitude, language)
    mess = f'Погода в городе {city}\nТемпература: {temp} °C\n{desc}'
    bot.send_message(message.chat.id, mess)


bot.polling(none_stop=True)
