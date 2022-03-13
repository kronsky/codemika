
# класс для создания покупателя
class Consumer:

    __consumer_id = 0
    __consumers = {}

    def __init__(self, name, surname):
        Consumer.__consumer_id += 1
        self.__consumer_id = Consumer.__consumer_id
        self.name = name
        self.surname = surname
        self.shopping_list = None
        if self.name and self.surname:
            Consumer.__consumers[self.__consumer_id] = f'{self.name} {self.surname}'
        # =>> если имя и фамилия есть, храним их в ввиде словаря, ок

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            # =>> Сеттеры это всегда хорошо :)
            # =>> А что если пользователь введёт имя '{d932&#I)=--FF__' ?
            # =>> А если какой-нибудь код введёт стрингом?
            # =>> Я думаю тут лучше всего использовать регулярные выражения
            self.__name = name
        else:
            raise ValueError('Invalid data type!')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) == str:
            self.__surname = surname
        else:
            raise ValueError('Invalid data type!')

    def get_consumer_personal_info(self):
        print(' Consumer personal information:')
        print(f'{self.__consumer_id}: {self.name} {self.surname}')

    @classmethod
    def get_consumers(cls):
        return Consumer.__consumers

    # =>> Не совсем понимаю зачем нам @classmetod?
    # =>> Я думаю тут можно использовать обычный @staticmethod:
    # =>> @staticmethod
    # =>> def get_consumers():
    # =>>       return Consumer.__consumers

    def items_bought(self, consumer_orders):                                    # Отслеживание заказов и итоговой стоимости покупки
        for order in consumer_orders:
            print(f'{order.get_consumer_orders()}')
            print(f'{order.get_total_price()}')
        # =>> Если в списке заказов пользователя есть заказы выводим словарь заказов
        # =>> и их стоимость
        # =>> Все отлично, но бы отправлял это с помощью return, а не выводом в консоль
        # =>> мало ли, что мы захотим делать с этой информацией в дальнейшем


# Список товаров для покупки
class ShoppingList:

    def __init__(self):
        self.__items_to_buy = list()

    def __str__(self):
        print(" Consumer's shopping list:")
        return f'{self.__items_to_buy}'

    def add_item_to_shopping_list(self, item):                                   # Добавление наименования товара в список
        if item not in self.__items_to_buy:
            # =>> Если итема нет в списке продуктов, кладём его туда
            self.__items_to_buy.append(item)
        else:
            raise ValueError(f'{item} is already in a shopping list!')
            # =>> иначе вываливаем исключение
            # =>> А если пользователь захочет купить два одинковых итема?

    def delete_item_from_shopping_list(self, item):                              # Удаление наименования товара из списка
        if item in self.__items_to_buy:
            self.__items_to_buy.remove(item)
        else:
            raise ValueError(f'There is no {item} in a shopping list!')
        # =>> Вываливаем итем из списка покупок, все ок
