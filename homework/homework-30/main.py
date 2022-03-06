# https://app.diagrams.net/#G10IFdUqxL_KDBJ2afESk_7QzssxWexnwS
import item, catalog, user

u1 = user.User('Ивван', 'Петров', '+79997652356')
u2 = user.User('Игорь', 'Смирнов', '+79875672334')

i1 = item.Item('Ноутбук ASUS ROG Zephyrus G14 GA401QM-K2100T', 'Quad HD 2K IPS, AMD Ryzen 9 5900HS, RAM 32 ГБ, SSD 1000 ГБ, GeForce RTX 3060', '17099d9')
i2 = item.Item('Робот-пылесос Xiaomi Mi Robot Vacuum Mop', 'Уборка - сухая/влажная, пылесборник - 0.6 л, ограничитель зоны, док-станция', 22999)
i3 = item.Item('Телевизор LED Philips 50PUS7406/60', '4K UltraHD, 3840x2160, DVB-S2, DVB-S, DVB-C, DVB-T2, Wi-Fi, Android TV, HDMI х 4, USB х 2', 51999)

cat_appliances = catalog.Catalog('Appliances')
cat_computers = catalog.Catalog('Computers')
cat_notebooks = catalog.Catalog('Computers', cat_computers)
cat_multimedia = catalog.Catalog('Multimedia')
cat_tv = catalog.Catalog('TV', cat_multimedia)

print()
print(i1)
print(i2)
print(i3)
print()
print(u1)
print(u2)
print()

