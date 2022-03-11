# Все задумки вроде-бы реализовал. Если у проверяющего возникнут
# вопросы - звоните, пишите, на все отвечу.
# С каталогами не стал заморачиваться, не хватает времени.
# UML добавлю 11 марта вечером.
from user import *

# создаём администратора
administrator = Administrator('Админ', 'Петрович', '+79875987345')

# берём пользователей из базы
userbase = UserDatabase()

# берём товары из базы
itembase = ItemDatabase()

# совершаем покупки
# понятно, что работая с БД мы бы использовали id,
# но в текущих условиях и для наглядности у пользователя будем брать
# номер телефона, а у товара наименование как уникальные значения

# создаём заказ:
order_1 = Order(userbase.get_user(1).phone)
# добавляем итемы:
order_1.add_item(itembase.get_item(3).title)
order_1.add_item(itembase.get_item(1).title)
# совершаем покупку:
order_1.buy()
# покупка второго пользователя:
order_2 = Order(userbase.get_user(2).phone)
order_2.add_item(itembase.get_item(2).title)
order_2.buy()
# покупка третьего пользователя:
order_3 = Order(userbase.get_user(3).phone)
order_3.add_item(itembase.get_item(7).title)
order_3.add_item(itembase.get_item(4).title)
order_3.add_item(itembase.get_item(2).title)
order_3.buy()
# первый пользователь совершает вторую покупку:
order_4 = Order(userbase.get_user(1).phone)
order_4.add_item(itembase.get_item(5).title)
order_4.buy()
print()

print('=> список всех совершенных заказов: ')
Order.print_orders()
print()

print('=> список покупок пользователей: ')
print(userbase.get_user(1), 'купил:', userbase.get_user(1).get_orders_by_user())
print(userbase.get_user(2), 'купил:', userbase.get_user(2).get_orders_by_user())
print()

print('=> количество проданных предметов: ')
print(itembase.get_item(2).title, 'продано в количестве:', itembase.get_item(2).get_counter_sold_item(), 'шт.')
print(itembase.get_item(5).title, 'продано в количестве:', itembase.get_item(5).get_counter_sold_item(), 'шт.')
print(itembase.get_item(8).title, 'продано в количестве:', itembase.get_item(8).get_counter_sold_item(), 'шт.')
print()

print('=> добавление в базу нового товара: ')
administrator.add_item(itembase)        # создадим новый товар
itembase.print_items()                  # смотрим все товары
print('=> удаление товара из базы: ')
administrator.remove_item(itembase)     # удалим товар
itembase.print_items()                  # смотрим все товары
print()
