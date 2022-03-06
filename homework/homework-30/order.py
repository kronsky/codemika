class Order:
    __last_id = 0

    def __init__(self):
        Order.__last_id += 1
        self.id = Order.__last_id
        self.user = None


class OrderDetails:
    __last_id = 0

    def __init__(self):
        OrderDetails.__last_id += 1
        self.id = OrderDetails.__last_id
        self.order = None
        self.item = None
