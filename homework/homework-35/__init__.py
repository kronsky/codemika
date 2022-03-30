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
    name = message.from_user.first_name
    bot.send_message(message.chat.id, text='Привет, ' + name, reply_markup=menu)


@bot.message_handler(commands=['get'])
def get(message):
    files_list = filestore.get_files_list(message.chat.id)
    buttons = types.InlineKeyboardMarkup()
    for file in files_list:
        callback = 'get:' + file['filename']
        buttons.add(telebot.types.InlineKeyboardButton(text=file['filename'], callback_data=callback))
    bot.send_message(message.chat.id, text="Какой файл отправить?", reply_markup=buttons)


@bot.message_handler(commands=['del'])
def delete(message):
    files_list = filestore.get_files_list(message.chat.id)
    buttons = types.InlineKeyboardMarkup()
    for file in files_list:
        callback = 'del:' + file['filename']
        buttons.add(telebot.types.InlineKeyboardButton(text=file['filename'], callback_data=callback))
    bot.send_message(message.chat.id, text="Какой файл удалить?", reply_markup=buttons)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    files_list = filestore.get_files_list(call.message.chat.id)
    if call.data[:3] == 'get':
        for file in files_list:
            if file['filename'] == call.data[4:]:
                bot.send_document(call.message.chat.id, file['file_id'])
    elif call.data[:3] == 'del':
        for file in files_list:
            if file['filename'] == call.data[4:]:
                files_list.remove(file)
                filestore.write_list(call.message.chat.id, files_list)
        bot.send_message(call.message.chat.id, 'Файл ' + call.data[4:] + ' удалён')
    # убираем кнопки
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Введи команду или загрузи файл')


@bot.message_handler(content_types=['document'])
def up_document(message):
    document_id = message.document.file_id
    filename = message.document.file_name
    caption = message.caption
    file_info = bot.get_file(document_id)
    bot.send_message(message.chat.id, 'Файл ' + filename + ' сохранён. ' + 'Ссылка на файл: ' +
                     f'http://api.telegram.org/file/bot{config.telegram_token}/{file_info.file_path}')
    filestore.write_file_info(message.chat.id, document_id, filename, caption)


@bot.message_handler(content_types=['photo'])
def up_photo(message):
    bot.send_message(message.chat.id, 'Отправь фото документом без сжатия!')


bot.polling(none_stop=True)
