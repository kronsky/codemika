import telebot
import config
import filestore
from telebot import types

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_get = types.KeyboardButton('/get',)
    button_del = types.KeyboardButton('/del', )
    menu.add(button_get, button_del)
    bot.send_message(message.chat.id, text='...', reply_markup=menu)


@bot.message_handler(commands=['get'])
def get(message):
    files_list = filestore.get_files_list()
    buttons = types.InlineKeyboardMarkup()
    for file in files_list:
        callback = 'get:' + file['filename']
        buttons.add(telebot.types.InlineKeyboardButton(text=file['filename'], callback_data=callback))
    bot.send_message(message.chat.id, text="Какой файл отправить?", reply_markup=buttons)


@bot.message_handler(commands=['del'])
def delete(message):
    files_list = filestore.get_files_list()
    buttons = types.InlineKeyboardMarkup()
    for file in files_list:
        callback = 'del:' + file['filename']
        buttons.add(telebot.types.InlineKeyboardButton(text=file['filename'], callback_data=callback))
    bot.send_message(message.chat.id, text="Какой файл удалить?", reply_markup=buttons)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data[:3] == 'get':
        files_list = filestore.get_files_list()
        for file in files_list:
            if file['filename'] == call.data[4:]:
                bot.send_document(call.message.chat.id, file['file_id'])
    elif call.data[:3] == 'del':
        print('DEL: функция не доделана')
    # убираем кнопки
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


@bot.message_handler(content_types=['text'])
def text(message):
    files_list = filestore.get_files_list()
    for file in files_list:
        if file['filename'] == message.text:
            bot.send_document(message.chat.id, file['file_id'])


@bot.message_handler(content_types=['document'])
def up_document(message):
    document_id = message.document.file_id
    filename = message.document.file_name
    caption = message.caption
    file_info = bot.get_file(document_id)
    if caption:
        # print(f'http://api.telegram.org/file/bot{config.telegram_token}/{file_info.file_path}')
        bot.send_message(message.chat.id, 'Файл ' + filename + ' сохранён. ' + 'Ссылка на файл: ' +
                         f'http://api.telegram.org/file/bot{config.telegram_token}/{file_info.file_path}')
        filestore.write_file_info(document_id, filename, caption)
    else:
        bot.send_message(message.chat.id, 'Не указана подпись файла!')


@bot.message_handler(content_types=['photo'])
def up_photo(message):
    bot.send_message(message.chat.id, 'Отправь фото документом без сжатия!')


bot.polling(none_stop=True)
