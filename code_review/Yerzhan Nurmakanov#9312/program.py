import consumer
import admin
import catalog

# =>> Приветсвую! прошу прощения если что-то не правильно понял, первый раз разбираю чужой код :)
# =>> Свои комментарии буду помечать символами =>>


# TESTING MY PROGRAM

# Создаем покупателя
simple_fellow = consumer.Consumer('Micky', 'Mouse')
simple_fellow.get_consumer_personal_info()                                      # Получаем персональную информацию о покупателе
# =>> для того чтобы не писать каждый раз имя файла для обращения к классу
# =>> можно импортировать сам класс из файла, например так:
# =>> from consumer import Consumer или from consumer import * для импорта всех классов
# =>> тогда можно сказать так: simple_fellow = Consumer('Micky', 'Mouse')


# Создаем администратора
admin = admin.Administrator('Taz', 'Mania')
admin.get_admin_personal_info()                                                 # Получаем персональную информацию об админе


# Создаем список товаров для покупки
simple_fellow.shopping_list = consumer.ShoppingList()
simple_fellow.shopping_list.add_item_to_shopping_list('Milk')
simple_fellow.shopping_list.add_item_to_shopping_list('Bread')
simple_fellow.shopping_list.add_item_to_shopping_list('Pencil')
print(simple_fellow.shopping_list)


# Создаем первый каталог
catalog1 = catalog.ShopCatalog('See, buy, fly')
print(catalog1.get_catalog_info())

catalog1.add_item_to_product_range('Milk', 50)
catalog1.add_item_to_product_range('Sugar', 65.5)
catalog1.add_item_to_product_range('Salt', 35)
catalog1.add_item_to_product_range('Tea', 40)
catalog1.add_item_to_product_range('Pepper', 20)
print(catalog1.get_product_range())


# Создаем второй каталог

catalog2 = catalog.ShopCatalog('Gajets')
print(catalog2.get_catalog_info())

catalog2.add_item_to_product_range('Iphone', 500)
catalog2.add_item_to_product_range('Ipad', 650.50)
catalog2.add_item_to_product_range('Chromebook', 700)

print(catalog2.get_product_range())


# Создаем первую корзину для покупателя (его заказы (ордеры))
Micky_order1 = catalog.ConsumerOrder(simple_fellow)

Micky_order1.get_counsumer_info()                                                # Получаем персональную информацию обладателя корзины (покупающего товары)

Micky_order1.order_item('Milk', catalog1)                                        # Добавляем товар из каталога
Micky_order1.order_item('Sugar', catalog1)
Micky_order1.order_item('Tea', catalog1)
# Micky_order.order_item('Ipad', catalog1)

# =>> Микки Маус решил попить чаю с молоком и сахаром :)

print(Micky_order1.get_consumer_orders())                                        # Получаем информацию о товарах в корзине

Micky_order1.get_total_price()

# Создаем вторую корзину для покупателя (его заказы (ордеры))
Micky_order2 = catalog.ConsumerOrder(simple_fellow)

Micky_order2.get_counsumer_info()                                                # Получаем персональную информацию обладателя корзины (покупающего товары)

Micky_order2.order_item('Iphone', catalog2)                                      # Добавляем товар из каталога
Micky_order2.order_item('Ipad', catalog2)
Micky_order2.order_item('Chromebook', catalog2)

# Получаем информацию о заказах покупателя
simple_fellow.items_bought([Micky_order1, Micky_order2])                         # Метод принимает в качестве аргументов заказы


# Пример реализации методов админа
layman = consumer.Consumer('Looney', 'Toon')
layman.shopping_list = consumer.ShoppingList()
layman.shopping_list.add_item_to_shopping_list('Laptop')
layman.shopping_list.add_item_to_shopping_list('Smartphone')

admin.track_consumers([simple_fellow, layman])
admin.track_catalogs([catalog1, catalog2])
