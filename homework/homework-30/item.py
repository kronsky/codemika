class Item:
    __last_id = 0
    __items = dict()

    def __init__(self, title, description, price):
        Item.__last_id += 1
        self.__id = Item.__last_id
        self.title = title
        self.description = description
        self.price = price
        Item.__items[self.__id] = self

    def __str__(self):
        return 'id=' + str(self.__id) + ',' + str(self.title)

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


class ItemList:
    __last_id = 0

    def __init__(self):
        ItemList.__last_id += 1
        self.id = ItemList.__last_id
        self.item = None
        self.catalog = None
