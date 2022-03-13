class ShopCatalog:
    __catalog_id = 0

    def __init__(self, catalog_name):
        self.catalog_name = catalog_name
        ShopCatalog.__catalog_id += 1
        self.__catalog_id = ShopCatalog.__catalog_id
        self.product_range = dict()

    def add_item_to_product_range(self, item, price):
        if type(item) == str and isinstance(price, (int, float)):
            self.product_range[item] = price
        else:
            raise ValueError('Invalid data types!')

    def delete_item_from_product_range(self, item):
        del self.product_range[item]
        # =>> А если итема в product_range нет?

    def get_product_range(self):
        print(f"Following items are in a '{self.catalog_name}' catalog:")
        return self.product_range

    def get_catalog_info(self):
        print(' ID and catalog name:')
        return f'{self.__catalog_id}: {self.catalog_name}'


class ConsumerOrder:

    def __init__(self, consumer):
        self.consumer = consumer
        self.items_ordered = dict()

    def get_counsumer_info(self):
        print(f'This basket belongs to {self.consumer.name}')

    def order_item(self, item, catalog):
        if item in catalog.product_range:
            self.items_ordered[item] = catalog.product_range[item]
            print(f"{item} was added to {self.consumer.name}'s basket")
        else:
            raise ValueError(f'There is no {item} in a {catalog.catalog_name} catalog!')

    def delete_item_from_basket(self, item):
        if item in self.items_ordered:
            del self.items_ordered[item]
        else:
            raise ValueError(f'There is no {item} in a basket!')

    def get_consumer_orders(self):
        print(f'{self.consumer.name} ordered following items:')
        return self.items_ordered

    def get_total_price(self):
        print(' Total price:')
        return sum(self.items_ordered.values())

    # =>> Тут методы для работы с корзиной, вроде бы все понятно
