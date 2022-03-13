import hashlib


def hash_string(string):
    temp = str(hashlib.sha256(string.encode('utf-8')).hexdigest())
    return temp[0:10]


class Item:

    def __init__(self, item_name, price, item_count):
        self.item_id = hash_string(item_name + price)
        # Очень интересная задумка использовать хэш в качестве id товара.

        self.item_name = item_name
        self.description = price
        self.item_count = int(item_count)

    def increase_amount(self, count):
        self.item_count += count

    def decrease_amount(self, count):
        self.item_count -= count

    def amount(self):
        return self.item_count

    def get_id(self):
        return self.item_id

    def set_amount(self, new_amount):
        self.item_count = new_amount

    def __str__(self):
        return str(f'{self.item_id}, {self.item_name}, {self.description}, {self.item_count}')
