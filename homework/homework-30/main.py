# https://app.diagrams.net/#G10IFdUqxL_KDBJ2afESk_7QzssxWexnwS

class User:
    __last_id = 0

    def __init__(self, name, surname):
        User.__last_id += 1
        self.id = User.__last_id
        self.name = name
        self.surname = surname


class Item:
    __last_id = 0

    def __init__(self, title, description, price):
        Item.__last_id += 1
        self.id = Item.__last_id
        self.title = title
        self.description = description
        self.price = price


class Catalog:
    __last_id = 0

    def __init__(self):
        Catalog.__last_id += 1
        self.id = Catalog.__last_id
        self.catalog = None
        self.itemlist = None


class ItemList:
    __last_id = 0

    def __init__(self):
        ItemList.__last_id += 1
        self.id = ItemList.__last_id
        self.item = None
        self.catalog = None


class Order:
    __last_id = 0

    def __init__(self):
        Order.__last_id += 1
        self.id = Order.__last_id
        self.user = None


class OrderDetails:
    __last_id = 0

    def __init__(self):
        OrderDetails.__last_id += 1
        self.id = OrderDetails.__last_id
        self.order = None
        self.item = None
