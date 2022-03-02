def multiplication(a, b):
    result = []
    # умножение количества концертов на гонорар для получения общей прибыли
    # если исполнитель играет только на новогодних корпоративах то считаем
    # только декабрь
    if len(a) == 12 and len(b) == 12:
        for i in range(len(a)):
            # в задаче есть исполнители, получившие гонорар за 0 концертов
            # если концертов 0, но гонорар есть - умножать его на ноль не будем
            # если концерты есть но гонорар 0 - ок, бесплатные концерты :)
            if a[i] == 0 and b[i] != 0:
                a[i] = 1
            result.append(a[i] * b[i])
    if len(a) == 1 and len(b) == 1:
        if a[0] == 0 and b[0] != 0:
            a[0] = 1
        result = [0] * 11
        result.append(a[0] * b[0])
    return result


def search_in_list(data, x):
    style_set = set()
    for artists in range(len(data)):
        style_set.add(data[artists][x])
    return list(style_set)


def musical_style_max(data):
    # определяем, какие жанры есть
    musical_style = search_in_list(data, 'musical_style')
    # в цикле по списку иполителей, вложенным в цикл по жанрам, если стиль
    # исполнителя соответствует текущему стилю, считаем гонорар в год
    style_max = {}
    for style in musical_style:
        fee_sum = 0
        artists = 0
        for artists_index in range(len(data)):
            if data[artists_index]['musical_style'] == style:
                artists = artists + 1
                fee_sum += sum(multiplication(data[artists_index]['monthly_calendar'], data[artists_index]['fee']))
        # поделим общий гонорар по жанру на количество исполнителей
        # положим в словарик для удобства и найдём максимальное значение
        fee_sum /= artists
        style_max[style] = fee_sum
    return max(style_max, key=style_max.get)


def monthly_max_fee(data, style):
    # из условия задачи я понял, что нужно найти месяц,в который самые большие гонорары за один концерт
    # и количество концертов учитывать не надо, потому что вопрос "сколько можно заработать"
    # а не "сколько исполнители заработали". Ведь количество концертов зависит от конкретного исполнителя
    artists_style = []
    for artists_index in range(len(data)):
        if data[artists_index]['musical_style'] == style:
            artists_style.append(data[artists_index])
    monthly_fee = [0] * 12
    for artists_index in artists_style:
        if len(artists_index['fee']) == 12:
            for index in range(12):
                monthly_fee[index] += artists_index['fee'][index]
        if len(artists_index['fee']) == 1:
            monthly_fee[11] += artists_index['fee'][0]
    return monthly_fee.index(max(monthly_fee))


def name_min_fee(data, monthly):
    artists_names = search_in_list(data, 'name')
    artists_min = {}
    for name in artists_names:
        fee_sum = 0
        for artists_index in range(len(data)):
            if data[artists_index]['name'] == name:
                fee_mul = multiplication(data[artists_index]['monthly_calendar'], data[artists_index]['fee'])
                fee_sum += fee_mul[monthly]
        artists_min[name] = fee_sum
    # убираем из словаря нулевые значения, чтобы не учитывать группы с нулевым гонораром
    artists_min = {key: val for key, val in artists_min.items() if val != 0}
    return min(artists_min, key=artists_min.get)


file = {
  "name": "Помесячное количество выступлений и гонораров на 2021 год",
  "artists": [
    {
      "name": "Паста",
      "musical_style": "rap",
      "monthly_calendar": [20, 14, 13, 19, 27, 22, 14, 7, 23, 6, 5, 6],
      "fee": [2, 21, 26, 0, 11, 0, 14, 12, 9, 25, 17, 18]
    },
    {
      "name": "Клавец",
      "musical_style": "rap",
      "monthly_calendar": [6, 2, 0, 2, 6, 0, 2, 7, 3, 9, 1, 1],
      "fee": [3, 6, 0, 1, 4, 6, 2, 7, 3, 0, 7, 4]
    },
    {
      "name": "Злой Мух",
      "musical_style": "rap",
      "monthly_calendar": [23, 18, 21, 20, 4, 6, 22, 13, 19, 9, 9, 25],
      "fee": [13, 16, 10, 27, 1, 6, 1, 4, 10, 19, 7, 23]
    },
    {
      "name": "Мультик",
      "musical_style": "rap",
      "monthly_calendar": [6, 23, 8, 10, 18, 7, 11, 11, 25, 10, 5, 9],
      "fee": [16, 21, 16, 26, 3, 28, 28, 19, 3, 25, 17, 0]
    },
    {
      "name": "Опера",
      "musical_style": "rap",
      "monthly_calendar": [25, 5, 17, 16, 12, 29, 24, 15, 2, 24, 6, 1],
      "fee": [24, 29, 0, 26, 12, 0, 17, 8, 25, 17, 17, 9]
    },
    {
      "name": "Натулис Пампулис",
      "musical_style": "rap",
      "monthly_calendar": [7, 20, 18, 12, 5, 28, 20, 11, 21, 2, 18, 4],
      "fee": [6, 28, 27, 11, 1, 20, 8, 23, 2, 23, 6, 15]
    },
    {
      "name": "Паста",
      "musical_style": "rock",
      "monthly_calendar": [14, 22, 15, 15, 22, 19, 4, 13, 23, 21, 2, 3],
      "fee": [4, 7, 15, 28, 27, 4, 13, 13, 5, 7, 20, 17]
    },
    {
      "name": "Мультик",
      "musical_style": "rock",
      "monthly_calendar": [6, 6, 15, 10, 2, 17, 25, 29, 18, 26, 7, 28],
      "fee": [12, 12, 15, 4, 23, 5, 26, 17, 9, 17, 0, 4]
    },
    {
      "name": "Злой Мух",
      "musical_style": "rock",
      "monthly_calendar": [0, 8, 4, 21, 1, 23, 24, 14, 6, 27, 28, 11],
      "fee": [11, 4, 8, 26, 0, 28, 24, 20, 8, 8, 24, 11]
    },
    {
      "name": "Мультик",
      "musical_style": "djs",
      "monthly_calendar": [25, 20, 14, 18, 17, 3, 18, 18, 2, 24, 9, 6],
      "fee": [19, 9, 11, 23, 13, 27, 16, 12, 1, 29, 21, 24]
    },
    {
      "name": "Опера",
      "musical_style": "djs",
      "monthly_calendar": [7, 21, 1, 25, 16, 0, 14, 9, 18, 18, 9, 3],
      "fee": [25, 12, 2, 9, 6, 29, 21, 16, 18, 23, 6, 14]
    },
    {
      "name": "Натулис Памулис",
      "musical_style": "djs",
      "monthly_calendar": [19, 21, 4, 4, 4, 4, 25, 22, 22, 11, 16, 3],
      "fee": [7, 13, 25, 17, 6, 5, 25, 22, 19, 22, 3, 9]
    }
  ]
}

msm = musical_style_max(file['artists'])
print('Музыкальный стиль, который приносит музыкантам больше всего денег:', msm)
mmf = monthly_max_fee(file['artists'], msm)
print('Номер месяца в году, в котором на этом стиле можно заработать больше всего:', mmf + 1)
nmf = name_min_fee(file['artists'], mmf)
print('Название музыкальной группы, которая меньше всего зарабатывает в этом месяце:', nmf)
