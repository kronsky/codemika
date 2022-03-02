class TriangleChecker(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # попытка переобразовать введенные данные в тип float
    # в случае исключения введено было не число (не int и не float)
    def __chek_int(self):
        try:
            self.a = float(self.a)
            self.b = float(self.b)
            self.c = float(self.c)
            return True
        except:
            print('Нужно вводить только числа!')

    # проверка на отрицательные числа
    def __chek_negative(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            print('С отрицательными числами ничего не выйдет!')
        else:
            return True

    # если проверки пройдены вычисляем можно ли построить треугольник
    def is_triangle(self):
        if self.__chek_int() and self.__chek_negative():
            if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                print('Ура, можно построить треугольник!')
            else:
                print('Жаль, но из этого треугольник не сделать.')


a = input('Введите длину первого отрезка: ')
b = input('Введите длину второго отрезка: ')
c = input('Введите длину третьего отрезка: ')

triangle = TriangleChecker(a, b, c)
triangle.is_triangle()
