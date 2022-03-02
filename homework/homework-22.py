import random
import datetime

# чтение городов из файла в список
with open('homework-22-cities.file') as cities_file:
    cities_list = cities_file.read().splitlines()

# список городов, которые уже назывались
cities_list_past = []
# индикатор конца игры
end_game = False
# счетчик оставшихся попыток
counter = 0


# запись события в log файл
def wrile_file(line):
    with open('homework-22-log.txt', mode='a') as file:
        time = str(datetime.datetime.now().strftime (("%d.%m.%Y %H:%M:%S")))
        file.writelines(time + ' ' + line)


# последний названный город
def last_citi():
    return cities_list_past[len(cities_list_past) - 1]


# последняя буква последнегго названного города
def last_letter():
    problem_letter = ['ц', 'ф', 'з', 'ш', 'э', 'ы']
    letter = last_citi()[-1]
    # если город заканчивается на ь, то берем предыдущую бувку
    if letter == 'ь':
        return last_citi()[-2]
    # если город заканчивается на бувку, на которую нет названий городов
    # то берем первую букву предыдущего города
    elif letter in problem_letter:
        return last_citi()[0].lower()
    # если город заканчивается на бувку "й" и йошкар-Ола уже называлась, берем букву "и"
    elif letter == 'й' and 'Йошкар-Ола' in cities_list_past:
        return 'и'
    else:
        return letter


# поиск города по букве
def city_search():
    lletter = last_letter()
    city_on_letter = []
    # создаем список городов на заданную букву
    for city in cities_list:
        if lletter == city[0].lower():
            city_on_letter.append(city)
    # если полученный список не пустой то берем из него случайный город
    if len(city_on_letter) != 0:
        return city_on_letter[random.randint(0, len(city_on_letter) - 1)]
    else:
        # иначе конец игры
        global end_game
        end_game = True
        wrile_file('Пользователь выиграл' + '\n')
        print('Вы выиграли! Поздравляю!')


# уведомление о количестве попыток
def number_of_attempts():
    print('У вас осталось: ' + str(4 - counter) + ' попыток')
    wrile_file('У пользвателя осталось: ' + str(4 - counter) + ' попыток' + '\n')


# проверка введенного пользователем города
def chek_city(city):
    if city not in cities_list and city not in cities_list_past:
        print('Такого города не существует')
        wrile_file('Пользователь ввел неверный город: ' + city + ' (такого города не существует)' + '\n')
        number_of_attempts()
    elif city in cities_list_past:
        print('Этот город уже назывался')
        wrile_file('Пользователь ввел неверный город: ' + city + ' (этот город уже назывался)' + '\n')
        number_of_attempts()
    elif city[0].lower() != last_letter():
        print('Город начинается не на ту букву')
        wrile_file('Пользователь ввел неверный город: ' + city + ' (город начинается не на ту букву)' + '\n')
        number_of_attempts()
    else:
        return True


# ход компьютера
def turn_computer():
    # если список названных голодов пустой, то это первый ход
    if len(cities_list_past) == 0:
        city = cities_list[random.randint(0, len(cities_list) - 1)]
    else:
        city = city_search()
    global end_game
    # если гра не закончена то переносим город из общего списка
    # в список уже названных городов
    if not end_game:
        wrile_file('Компьютер выбрал город ' + city + '\n')
        print('Компьютер выбрал город: ', city)
        cities_list_past.append(city)
        cities_list.remove(city)


# ход пользователя
def turn_user():
    print('Введите город на букву: ', last_letter().upper())
    city = input('==>> ')
    # введенный город прошел проверку то переносим город из общего списка
    # в список уже названных городов
    if chek_city(city):
        wrile_file('Пользователь выбрал город ' + city + '\n')
        cities_list_past.append(city)
        cities_list.remove(city)
    else:
        # иначе забираем одну из пяти попытку и повторяем фукнцию
        # при пяти неверных попытках завершаем игру
        global counter
        counter += 1
        if counter < 5:
            turn_user()
        else:
            global end_game
            end_game = True
            wrile_file('Пользователь проиграл' + '\n')
            print('Вы проиграли')


# пока игра не закончена запускаем цикл ходов
while not end_game:
    turn_computer()
    if not end_game:
        turn_user()
