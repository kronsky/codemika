from CLASS_Administrator import *
from CLASS_Catalog import Catalog
from CLASS_User import User
from data_items import data

'''
"Этот магазинчик умеет:
1. Хозяин - администратор, должен уметь, добавлять товары в каталог. 
   То есть только у Администратора есть необходимые методы
2. Товары находятся в общем каталоге.
3. Пользователь выбирает товар для выбора, после чего добавляет товар в корзину. 
'''

# Приветсвую! прошу прощения если что-то не правильно понял, первый раз разбираю чужой код :)

# Не совсем понял систему каталогов, зачем загружать товары в сам каталог, но задумка интересная 

catalog = Catalog(data)
# Создание каталога, передав ему список товаров.
# То есть нет едиой базы товаров, идет жесткое разделение на каталоги.
# А что будет если пользователь захочет купить товары из разных каталогов?
# И сможем ли мы в таком случае  вести единую статистику по проданным товарам,
# или покупкам пользователя ...

admin = Administrator(catalog)
# Администратор получает сам каталог и использует его методы через интерфейс, вопросов нет

admin.add_item("Rom Capitan", "200", 5)
catalog.print()
admin.del_item('18779b2d9f')
# Before Oleg's shopping
catalog.print()

user_oleg = User(catalog)
# Жесткая привязка пользователя к определенному каталогу, возвращаясь к
# предыдущему вопросу, как быть если каталог не один?

print(user_oleg.order_item('ce9da1300b', 2))
# After Oleg's shopping
catalog.print()