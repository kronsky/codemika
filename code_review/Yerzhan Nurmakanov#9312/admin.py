import consumer
import catalog
# =>> в admin.py импортируется catalog, он же импортируется в program.py
# =>> можно в admin.py ипортировать все классы из catalog.py: from catalog import *
# =>> а в catalog.py импортировать все классы из admin.py: from admin import *
# =>> тогда в program.py импортируются все классы из admin.py, и рекурсивно из catalog.py


class Administrator:

    # =>> Админ не наследует сласс обычного юзера, наверное потому что он не потребитель, логично :)

    __admin_id = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Administrator.__admin_id += 1
        self.__admin_id = Administrator.__admin_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            # =>> Аналогичная с consumer ситуация, в стринг можно положить любые символы,
            # =>> лучше использовать регулярное выражение
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

    def get_admin_personal_info(self):
        print(' Administrator personal information:')
        print(f'{self.__admin_id}: {self.name} {self.surname}')

    def track_consumers(self, consumers):
        print(' Information about consumers:')
        for consumer in consumers:
            consumer.get_consumer_personal_info()
            if consumer.shopping_list:
                print(consumer.shopping_list)
            print('')
        # =>> В этом методе нет взаимодействия с экземпляром класса,
        # =>> можно считать его статическим и использовать декоратор @staticmethod
        # =>> Все нижеперечисленные классы тоже будут статическими,
        # =>> и должны иметь декторатор @staticmethod. Self тоже нужно убрать.
        # =>> То есть выглядеть это должно примерно так:
        # =>> @staticmethod
        # =>> def track_consumers(consumers):
        # =>>     print(' Information about consumers:')
        # =>>     for consumer in consumers:
        # =>>         consumer.get_consumer_personal_info()
        # =>>         if consumer.shopping_list:
        # =>>             print(consumer.shopping_list)
        # =>>         print('')


    def track_catalogs(self, catalogs):
        print(' Information about catalogs and their product range:')
        for catalog in catalogs:
            print(catalog.get_catalog_info())
            print(catalog.product_range)
            print('')

    def add_item_to_catalog(self, item, price):
        if item and price:
            catalog.ShopCatalog.add_item_to_product_range(item, price)

    def delete_item_from_catalog(self, item):
        catalog.ShopCatalog.delete_item_from_product_range(item)





