from order import *


class Item:
    __last_id = 0

    def __init__(self, title, description, price):
        Item.__last_id += 1
        self.__id = Item.__last_id
        self.title = title
        self.description = description
        self.price = price

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


class Catalog:
    __last_id = 0

    def __init__(self, name, catalog=None):
        Catalog.__last_id += 1
        self.id = Catalog.__last_id
        self.name = name
        self.catalog = catalog
        self.itemlist = None

    def __str__(self):
        return self.name


class ItemDatabase:
    def __init__(self):
        self._item_database = {
            1: Item('Ноутбук ASUS ROG Zephyrus', 'Ryzen 9 5900HS, RAM 32 ГБ, SSD 1TБ, RTX 3060', 167987),
            2: Item('Робот-пылесос Xiaomi', 'Уборка - сухая/влажная, пылесборник - 0.6 л, ограничитель зоны', 22999),
            3: Item('Телевизор LED Philips', '4K, Wi-Fi, Android TV, HDMI х 4, USB х 2', 51999),
            4: Item('Ноутбук Apple MacBook Air', '2560x1600, IPS, Apple M1, RAM 16 ГБ, SSD 256 ГБ,', 169999),
            5: Item('Электрочайник Polaris', '1.5 л, 2150 Вт, скрытый нагревательный элемент, фильтр', 3599),
            6: Item('Утюг Philips', '2600 Вт, подошва - керамика, титан', 6499),
            7: Item('Кофемашина DeLonghi', 'эспрессо, исп. кофе - молотый, зерновой, 1450 Вт, 1.4 л,', 69999),
            8: Item('Холодильник LG GA-B459CLWL', '341 л, No Frost, дисплей, 59.5 см х 186 см х 68.2 см', 68299)
        }

    def get_item(self, item_id):
        item = self._item_database.get(item_id)
        if not item:
            raise ValueError(item_id)
        return item

    # def _create_item(self, title, description, price):
    #     return Item(title, description, price)
