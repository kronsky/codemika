import telebot
import config
import openweathermap as weather
from telebot import types
import os
import random

bot = telebot.TeleBot(config.telegram_token)


CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]


@bot.message_handler(commands=['start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('1')
    button_2 = types.KeyboardButton('2')
    button_3 = types.KeyboardButton('3')
    button_4 = types.KeyboardButton('4')
    button_5 = types.KeyboardButton('5')

    menu.add(button_1, button_2)
    menu.add(button_3)
    menu.add(button_4, button_5)

    bot.send_message(message.chat.id, text='Привет, выбирай пункт меню', reply_markup=menu)
    #
    #
    #
    #
    # welcome_message = 'Привет! Это бот для определения погоды в твоей локации.'
    # menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # menu_item_location = types.KeyboardButton('Поделиться своим контактом', request_contact=True)
    # menu.add(menu_item_location)
    # bot.send_video_note(message.chat.id, 'DQACAgIAAxkBAAPbYj3UYIWbLt8NAg19kCtH7Ubb9tcAAt8WAALE7fBJCJd3xeRoUZ4jBA')
    # bot.send_message(message.chat.id, welcome_message, reply_markup=menu)


@bot.message_handler(content_types=['location'])
def get_weather(message):
    language = message.from_user.language_code
    latitude = message.location.latitude
    longitude = message.location.longitude
    desc, temp, city, icon = weather.get(longitude, latitude, language)
    mess = f'Погода в городе {city}\nТемпература: {temp} °C\n{desc}'
    img = open('./images/' + icon + '.png', 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['random'])
def get_random_image(message):
    directory = './images/'
    files = os.listdir(directory)
    index = random.randrange(len(files))
    img = open(directory + files[index], 'rb')
    bot.send_photo(message.chat.id, img)


@bot.message_handler(content_types=['video_note'])
def get_video_note(message):
    print(message)


bot.polling(none_stop=True)

