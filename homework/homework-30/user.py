import re
from item import *


class User:
    __last_id = 0

    def __init__(self, name, surname, phone):
        User.__last_id += 1
        self.__id = User.__last_id
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' ' + str(self.phone) + ' (id=' + str(self.__id) + ')'

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone):
            self.__phone = phone
        else:
            raise ValueError('Invalid phone number')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if re.fullmatch(r'[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?', name):
            self.__name = name
        else:
            raise ValueError('Invalid user name')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if re.fullmatch(r'[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?', surname):
            self.__surname = surname
        else:
            raise ValueError('Invalid user surname')

    def get_id(self):
        return self.__id

    # получаем список покупок пользователя
    def get_orders_by_user(self):
        order_list = []
        for order in Order.get_orders():
            if self.phone in order:
                order_list = order_list + order[self.phone]
        return order_list


class Administrator(User):
    __last_id = 0

    def __init__(self, name, surname, phone):
        super(Administrator, self).__init__(name, surname, phone)
        Administrator.__last_id += 1
        self.__id = Administrator.__last_id

    @staticmethod
    def add_item(itembase):
        title = input('Введите название товара: ')
        description = input('Введите описание товара: ')
        price = input('Введите стоимость товара: ')
        itembase.add_item(title, description, price)

    @staticmethod
    def remove_item(itembase):
        id_removable_item = int(input('Введите id товара, который нужно удалить: '))
        itembase.remove_item(id_removable_item)


class UserDatabase:
    def __init__(self):
        self._user_database = {
            1: User('Иван', 'Зайчиков', '+79997652356'),
            2: User('Евгений', 'Бочонкин', '+79875672334'),
            3: User('Мария', 'Капустина', '+79875987345'),
        }

    def get_user(self, user_id):
        user = self._user_database.get(user_id)
        if not user:
            raise ValueError(user_id)
        return user
