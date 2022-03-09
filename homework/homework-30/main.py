from item import Item, ItemList
from user import User, Administrator
from order import Order
from catalog import Catalog

# создаём пользователей
user_1 = User('Иван', 'Зайчиков', '+79997652356')
user_2 = User('Евгений', 'Бочонкин', '+79875672334')
user_3 = User('Мария', 'Капустина', '+79875987345')

# создаём администратора
administrator_1 = Administrator('Админ', 'Админович', '+79875987345')

# создаём товары
item_1 = Item('Ноутбук ASUS ROG Zephyrus G14 GA401QM-K2100T', 'Ryzen 9 5900HS, RAM 32 ГБ, SSD 1TБ, RTX 3060', 167987)
item_2 = Item('Робот-пылесос Xiaomi Mi Robot', 'Уборка - сухая/влажная, пылесборник - 0.6 л, ограничитель зоны', 22999)
item_3 = Item('Телевизор LED Philips 50PUS7406/60', '4K, Wi-Fi, Android TV, HDMI х 4, USB х 2', 51999)
item_4 = Item('Ноутбук Apple MacBook Air', '2560x1600, IPS, Apple M1, RAM 16 ГБ, SSD 256 ГБ,', 169999)
item_5 = Item('Электрочайник Polaris PWK 1712CGLD', '1.5 л, 2150 Вт, скрытый нагревательный элемент, фильтр', 3599)
item_6 = Item('Утюг Philips GC4563', '2600 Вт, подошва - керамика, титан', 6499)
item_7 = Item('Кофемашина DeLonghi ETAM 29.660.SB', 'эспрессо, исп. кофе - молотый, зерновой, 1450 Вт, 1.4 л,', 69999)
item_8 = Item('Холодильник LG GA-B459CLWL', '341 л, No Frost, дисплей, 59.5 см х 186 см х 68.2 см', 68299)

# создаём каталоги
cat_appliances = Catalog('Appliances')
cat_computers = Catalog('Computers')
cat_notebooks = Catalog('Notebooks', cat_computers)
cat_multimedia = Catalog('Multimedia')
cat_tv = Catalog('TV', cat_multimedia)

# совершаем покупки
# понятно, что работая с БД мы бы использовали id,
# но в текущих условиях у пользователя будем брать номер телефона,
# а у товара наименование как уникальные значения
order_1 = Order(user_1.phone)           # создаём заказ
order_1.add_item(item_3.title)          # добавляем итем
order_1.add_item(item_1.title)          # добавляем итем
order_1.buy()                           # совершаем покупку

order_2 = Order(user_2.phone)
order_2.add_item(item_2.title)
order_2.buy()

order_3 = Order(user_3.phone)
order_3.add_item(item_7.title)
order_3.add_item(item_4.title)
order_3.add_item(item_2.title)
order_3.buy()

order_4 = Order(user_1.phone)
order_4.add_item(item_5.title)
order_4.buy()

print()
# смотрим все заказы
Order.print_orders()
print()

# списки покупок пользователей
print(user_1, 'купил:', user_1.get_orders_by_user())
print(user_2, 'купил:', user_2.get_orders_by_user())
print()

# сколько продано предметов
print(item_2, 'продано в количестве:',   item_2.get_counter_sold_item(), 'шт.')
print(item_5, 'продано в количестве:',   item_5.get_counter_sold_item(), 'шт.')
print(item_8, 'продано в количестве:',   item_8.get_counter_sold_item(), 'шт.')
