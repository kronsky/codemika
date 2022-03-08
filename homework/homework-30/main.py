# https://app.diagrams.net/#G10IFdUqxL_KDBJ2afESk_7QzssxWexnwS
import item, catalog, user, order

# создаём пользователей
u1 = user.User('Ивван', 'Петров', '+79997652356')
u2 = user.User('Игорь', 'Смирнов', '+79875672334')

# создаём товары
i1 = item.Item('Ноутбук ASUS ROG Zephyrus G14 GA401QM-K2100T', 'Quad HD 2K IPS, AMD Ryzen 9 5900HS, RAM 32 ГБ, SSD 1000 ГБ, GeForce RTX 3060', 167987)
i2 = item.Item('Робот-пылесос Xiaomi Mi Robot Vacuum Mop', 'Уборка - сухая/влажная, пылесборник - 0.6 л, ограничитель зоны, док-станция', 22999)
i3 = item.Item('Телевизор LED Philips 50PUS7406/60', '4K UltraHD, 3840x2160, DVB-S2, DVB-S, DVB-C, DVB-T2, Wi-Fi, Android TV, HDMI х 4, USB х 2', 51999)

# создаём каталоги
cat_appliances = catalog.Catalog('Appliances')
cat_computers = catalog.Catalog('Computers')
cat_notebooks = catalog.Catalog('Notebooks', cat_computers)
cat_multimedia = catalog.Catalog('Multimedia')
cat_tv = catalog.Catalog('TV', cat_multimedia)

o1 = order.Order(u1)    # создаём заказ
o1.add_item(i1)         # добавляем итем
o1.add_item(i2)         # добавляем итем
o1.bay()                # совершаем покупку

o2 = order.Order(u2)    # создаём заказ
o2.add_item(i3)         # добавляем итем
o2.bay()                # совершаем покупку

print(o1)               # смотрим первый заказ
print(o2)               # смотрим второй заказ

print(o1.get_orders())  # получаем все заказы
