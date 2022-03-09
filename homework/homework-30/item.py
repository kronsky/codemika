from order import Order


class Item:
    __last_id = 0
    __items = []

    def __init__(self, title, description, price):
        Item.__last_id += 1
        self.__id = Item.__last_id
        self.title = title
        self.description = description
        self.price = price
        Item.__items.append(self)

    def __str__(self):
        return str(self.title) + ' (id=' + str(self.__id) + ')'

    @property
    def price(self):
        return self.__price

    # сеттер стоимости товара, проверка на инт
    @price.setter
    def price(self, price):
        try:
            self.__price = int(price)
        except ValueError:
            raise ValueError('Invalid price')

    def get_id(self):
        return self.__id

    # получаем количество проданных товаров
    def get_counter_sold_item(self):
        item_counter = 0
        for list_order in Order.get_orders():
            for dict_order in list_order.values():
                if self.title in dict_order:
                    item_counter += 1
        return item_counter


class ItemList:
    __last_id = 0

    def __init__(self):
        ItemList.__last_id += 1
        self.id = ItemList.__last_id
        self.item = None
        self.catalog = None
