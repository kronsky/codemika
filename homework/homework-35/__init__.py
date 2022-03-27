import telebot
import config
import filestore
from telebot import types

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('/get',)
    menu.add(button)
    bot.send_message(message.chat.id, text='...', reply_markup=menu)


@bot.message_handler(commands=['get'])
def get(message):
    files_list = filestore.get_files_list()
    for file in files_list:
        bot.send_message(message.chat.id, file['filename'])


@bot.message_handler(content_types=['text'])
def get_random_image(message):
    files_list = filestore.get_files_list()
    for file in files_list:
        if file['filename'] == message.text:
            print(file)
            bot.send_document(message.chat.id, file['file_id'])


@bot.message_handler(content_types=['document'])
def up_file(message):
    document_id = message.document.file_id
    filename = message.document.file_name
    caption = message.caption
    file_info = bot.get_file(document_id)
    if caption:
        print(f'http://api.telegram.org/file/bot{config.telegram_token}/{file_info.file_path}')
        bot.send_message(message.chat.id, 'Файл ' + filename + ' сохранён')
        filestore.write_file_info(document_id, filename, caption)
    else:
        bot.send_message(message.chat.id, 'Не указана подпись файла, укажите!')


@bot.message_handler(content_types=['photo'])
def up_file(message):
    print(message.json.photo.file_id)
    # document_id = message.document.file_id
    # filename = message.document.file_name
    # caption = message.caption
    # file_info = bot.get_file(document_id)
    # if caption:
    #     print(f'http://api.telegram.org/file/bot{config.telegram_token}/{file_info.file_path}')
    #     bot.send_message(message.chat.id, 'Файл ' + filename + ' сохранён')
    #     filestore.write_file_info(document_id, filename, caption)
    # else:
    #     bot.send_message(message.chat.id, 'Не указана подпись файла, укажите!')


bot.polling(none_stop=True)

