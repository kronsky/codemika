class User:

    def __init__(self, catalog):
        self.catalog = catalog
        self.order_for_user = []

    def order_item(self, id, amount):
        item_to_order = self.catalog.add_item_to_order(id, amount)
        # если я правильно понял, тут мы с помощью метода add_item_to_order
        # создаём копию значения словаря и задаём ему количество

        self.order_for_user.append(item_to_order)
        # добавляем её в список покупок

        print("--- User's order: ---")
        result = "\n".join([str(item) for item in self.order_for_user])
        # ну и в качестве результата выводим все элементы списка покупок

        return result

    def clear(self):
        self.order_for_user = []
