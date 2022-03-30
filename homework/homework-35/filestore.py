import json


def write_file_info(chat_id, file_id, filename, caption):
    with open('files.json', 'r', encoding='utf-8') as file:
        try:
            chats = json.load(file)
        except ValueError:
            chats = dict()
    chat_id = str(chat_id)
    if chat_id in chats:
        file = {
            'file_id': file_id,
            'filename': filename,
            'caption': caption
        }
        chats[chat_id].append(file)
    else:
        ch_dict = {chat_id: [{
            'file_id': file_id,
            'filename': filename,
            'caption': caption
        }]}
        chats.update(ch_dict)
    with open('files.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(chats, ensure_ascii=False))


def write_list(chat_id, filelist):
    chat_id = str(chat_id)
    with open('files.json', 'r', encoding='utf-8') as file:
        chats = json.load(file)
    chats[chat_id] = filelist
    with open('files.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(chats, ensure_ascii=False))


def get_files_list(chat_id):
    with open('files.json') as file:
        try:
            chats = json.load(file)
        except ValueError:
            chats = dict()
    chat_id = str(chat_id)

    if chat_id in chats:
        return chats[chat_id]
    else:
        return list()
    # сделать проверку не пустой ли джейсон
