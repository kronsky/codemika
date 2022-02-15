class Nikola(object):

    def __init__(self, name, old):
        self.name = name
        self.old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name != 'Николай':
            self.__name = 'Я не ' + name + ', а Николай'
        else:
            self.__name = name

    def getName(self):
        return "Имя пользователя: " + str(self.__name)

    def getOld(self):
        return "Возраст пользователя: " + str(self.old)


user_name = input('Ваше имя: ')
user_old = input('Ваш возраст: ')

user = Nikola(user_name, user_old)
print(user.getName())
print(user.getOld())
