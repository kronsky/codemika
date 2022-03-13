class Administrator:

    def __init__(self, catalog):
        self.catalog = catalog

    def add_item(self, item_name, item_description, item_amount):
        self.catalog.add_item(item_name, item_description, item_amount)

    def del_item(self, id):
        self.catalog.delete_item(id)
