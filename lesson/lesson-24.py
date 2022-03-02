class Address(object):
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return self.city + ', ' + self.street


class User(object):
    __last_id = 0

    def __init__(self, name):
        User.__last_id += 1
        self.__id = User.__last_id
        self.name = name
        self.__address = None

    # def set_address(self, address):
    #     if type(address) == Address:
    #         self.__address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if type(address) == Address:
            self.__address = address

    def __str__(self):
        return str(self.__id) + ', ' + str(self.name) + ', ' + str(self.__address)


addr = Address('Moscow', 'Leninskiy prospect')
usr = User('Иван')
usr = User('Пётр')
usr = User('Степан')
usr.address(addr)

print(usr)