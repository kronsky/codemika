from CLASS_Item import Item
import copy


class Catalog:

    def __init__(self, data):
        self.items_dict = {}
        for i in range(len(data)):
            new_item = Item(data[i].get('Item name'), data[i].get('Price'), data[i].get('Amount'))
            item_id = new_item.get_id()
            self.items_dict[item_id] = new_item
        # Создание итемов из элементов некой бд (списка товаров)
        # и засовывание их в словарь с ключами айдишниками
        # Не могу понять смысл сего действия, почему бы не работать со словарём в самой бд (data),
        # предварительно сотворив его там ...
        # Но думаю данная реализация тоже имеет место быть :)

    def print(self):
        print("--- Marketplace's catalog: ---")
        for key, value in self.items_dict.items():
            print(value.__str__())

    def add_item(self, item_name, item_description, item_amount):
        new_item = Item(item_name, item_description, item_amount)
        item_id = new_item.get_id()
        if item_id not in self.items_dict.keys():
            self.items_dict[item_id] = new_item
        else:
            self.items_dict[item_id].increase_amount(item_amount)
        return item_id
        # Создаем итем и id, если id отсутсвует в ключах словаря
        # то добавляем новый итем, если уже есть то просто увеличиваем его количество,
        # возвращаем id. Все четко и понятно

    def delete_item(self, id):
        self.items_dict.pop(id)

    def get_item(self, id):
        return self.items_dict[id]

    def add_item_to_order(self, id, amount):
        self.items_dict[id].decrease_amount(amount)         # уменьшаем количство товара на складе
        item_in_order = copy.deepcopy(self.items_dict[id])  # рекурсивная копия зачения словаря товаров по ключу
        item_in_order.set_amount(amount)                    # задаём количество товара в копии
        return item_in_order
