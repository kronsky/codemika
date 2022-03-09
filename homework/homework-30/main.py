# https://app.diagrams.net/#G10IFdUqxL_KDBJ2afESk_7QzssxWexnwS
import item, catalog, user, order

# создаём пользователей
u1 = user.User('Иван', 'Зайчиков', '+79997652356')
u2 = user.User('Евгений', 'Бочонкин', '+79875672334')
u3 = user.User('Мария', 'Капустина', '+79875987345')

# создаём товары
i1 = item.Item('Ноутбук ASUS ROG Zephyrus G14 GA401QM-K2100T', 'Ryzen 9 5900HS, RAM 32 ГБ, SSD 1TБ, RTX 3060', 167987)
i2 = item.Item('Робот-пылесос Xiaomi Mi Robot', 'Уборка - сухая/влажная, пылесборник - 0.6 л, ограничитель зоны', 22999)
i3 = item.Item('Телевизор LED Philips 50PUS7406/60', '4K, Wi-Fi, Android TV, HDMI х 4, USB х 2', 51999)
i4 = item.Item('Ноутбук Apple MacBook Air', '2560x1600, IPS, Apple M1, RAM 16 ГБ, SSD 256 ГБ,', 169999)
i5 = item.Item('Электрочайник Polaris PWK 1712CGLD', '1.5 л, 2150 Вт, скрытый нагревательный элемент, фильтр', 3599)
i6 = item.Item('Утюг Philips GC4563', '2600 Вт, подошва - керамика, титан', 6499)
i7 = item.Item('Кофемашина DeLonghi ETAM 29.660.SB', 'эспрессо, исп. кофе - молотый, зерновой, 1450 Вт, 1.4 л,', 69999)
i8 = item.Item('Холодильник LG GA-B459CLWL', '341 л, No Frost, дисплей, 59.5 см х 186 см х 68.2 см', 68299)

# создаём каталоги
cat_appliances = catalog.Catalog('Appliances')
cat_computers = catalog.Catalog('Computers')
cat_notebooks = catalog.Catalog('Notebooks', cat_computers)
cat_multimedia = catalog.Catalog('Multimedia')
cat_tv = catalog.Catalog('TV', cat_multimedia)

o1 = order.Order(u1)    # создаём заказ
o1.add_item(i3)         # добавляем итем
o1.add_item(i1)         # добавляем итем
o1.buy()                # совершаем покупку

o2 = order.Order(u2)
o2.add_item(i2)
o2.buy()

o3 = order.Order(u3)
o3.add_item(i7)
o3.add_item(i4)
o3.add_item(i2)
o3.buy()

o4 = order.Order(u1)
o4.add_item(i5)
o4.add_item(i6)
o4.add_item(i1)
o4.add_item(i4)
o4.buy()

order.Order.print_orders()

print()

# print(o1.get_orders())  # получаем все заказы
