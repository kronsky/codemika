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
        return 'id=' + str(self.__id) + ',' + str(self.user) + ',' + str(self.order_list)

    def add_item(self, item):
        self.order_list.append(item)

    def remove_item(self, item):
        self.order_list.remove(item)

    def bay(self):
        Order.__orders[self.__id] = self

    @staticmethod
    def get_orders():
        return Order.__orders

