import datetime


class Order:
    __last_id = 0
    __orders = dict()

    def __init__(self, user):
        Order.__last_id += 1
        self.__id = Order.__last_id
        self.user = user
        self.order_list = []
        self.__date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def __str__(self):
        return str(self.__id) + '. ' + str(self.user) + ' ' + str(self.order_list)

    def add_item(self, item):
        # добавляем id итема в список заказа
        self.order_list.append(item.get_id())

    def remove_item(self, item):
        self.order_list.remove(item)

    def buy(self):
        # якобы покупка
        # запись ордера в словарь
        Order.__orders[self.__id] = self

    @staticmethod
    def print_orders():
        for order in Order.__orders.items():
            print(order[1])

    @staticmethod
    def get_orders():
        return Order.__orders

    @staticmethod
    def get_last_id():
        return Order.__last_id

