import json


def write_file_info(file_id, filename, caption):
    with open('files.json') as file:
        try:
            filelist = json.load(file)
        except ValueError:
            filelist = []
    file = {
        'file_id': file_id,
        'filename': filename,
        'caption': caption
    }
    filelist.append(file)
    with open('files.json', 'w') as file:
        json.dump(filelist, file, ensure_ascii=False)


def get_files_list():
    with open('files.json') as file:
        try:
            filelist = json.load(file)
        except ValueError:
            filelist = []
    return filelist
