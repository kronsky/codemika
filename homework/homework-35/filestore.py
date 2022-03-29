import json
# сохранить в json
# with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
#     fh.write(json.dumps(data, ensure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл
# загрузить из json
# with open('data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
#     data = json.load(fh) #загружаем из файла данные в словарь data


def write_file_info(chat_id, file_id, filename, caption):
    with open('files.json', 'r', encoding='utf-8') as file:

        try:
            chats = json.load(file)
        except ValueError:
            chats = dict()

    if chat_id in chats:
        print('Key found')
    else:
        print('Key not found')
        ch_dict = {chat_id: [{
            'file_id': file_id,
            'filename': filename,
            'caption': caption
        }]}
        print(chats)
        print(ch_dict)
        chats.update(ch_dict)
        print(chats)

    with open('files.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(chats, ensure_ascii=False))


def write_list(filelist):
    with open('files.json', 'w') as file:
        json.dump(filelist, file, ensure_ascii=False)


def get_files_list():
    with open('files.json') as file:
        try:
            filelist = json.load(file)
        except ValueError:
            filelist = []
    return filelist
