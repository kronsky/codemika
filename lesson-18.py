# class User(object):
#     def __init__(self):
#         self.name = input()
#         self.surname = input()
#
#     def get_info(self):
#         print(self.name, self.surname)
#
#
# user1 = User()
# user2 = User()
# user3 = User()
#
# user3.get_info()
# user2.get_info()
# user1.get_info()


class User(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        print(self.name, self.surname)


user1 = User('Иван', 'Иванов')
user2 = User('Петр', 'Петров')
user3 = User('Николай', 'Николанв')

user3.get_info()
user2.get_info()
user1.get_info()
