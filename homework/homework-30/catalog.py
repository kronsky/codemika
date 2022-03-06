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