import re
import datetime
import order


class User:
    __last_id = 0
    __users = dict()

    def __init__(self, name, surname, phone):
        User.__last_id += 1
        self.__id = User.__last_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.__last_login = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        User.__users[self.__id] = self

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' ' + str(self.phone) + ' (id=' + str(self.__id) + ')'

    @property
    def phone(self):
        return self.__phone

    # сеттер телефонного номера, проверка через регулярное выражение
    @phone.setter
    def phone(self, phone):
        if re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone):
            self.__phone = phone
        else:
            raise ValueError('Invalid phone number')

    @property
    def name(self):
        return self.__name

    # сеттер имени пользователя, проверка через регулярное выражение
    @name.setter
    def name(self, name):
        if re.fullmatch(r'[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?', name):
            self.__name = name
        else:
            raise ValueError('Invalid user name')

    @property
    def surname(self):
        return self.__surname

    # сеттер фамилии пользователя, проверка через регулярное выражение
    @surname.setter
    def surname(self, surname):
        if re.fullmatch(r'[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?', surname):
            self.__surname = surname
        else:
            raise ValueError('Invalid user surname')

    def get_id(self):
        return self.__id

    def get_last_login(self):
        return self.__last_login

    @staticmethod
    def get_users_object():
        return User.__users
