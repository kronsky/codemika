import math


class Triangle(object):
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def area(self):
        area = 0.5 * abs((self.bx - self.ax) * (self.cy - self.ay) - (self.cx - self.ax) * (self.by - self.ay))
        return area

    def perimeter(self):
        ab = math.sqrt(pow(self.bx - self.ax, 2) + pow(self.by - self.ay, 2))
        bc = math.sqrt(pow(self.cx - self.bx, 2) + pow(self.cy - self.by, 2))
        ca = math.sqrt(pow(self.ax - self.cx, 2) + pow(self.ay - self.cy, 2))
        return ab + bc + ca

    def medianpoint(self):
        # координаты точки k (середина отрезка bc)
        kx = (self.bx + self.cx) / 2
        ky = (self.by + self.cy) / 2
        # отрезок ak (медиана) точкой пересечения делится в отношении 2:1, считая от вершины a
        # Хs = (Xa + λ * Xk) / (1 + λ) и Ys = (Ya + λ * Yk) / (1 + λ), λ = 2 / 1
        s = [(self.ax + 2 * kx) / 3, (self.ay + 2 * ky) / 3]
        return s


triangle = Triangle(int(input('Координата точки a по x: ')), int(input('Координата точки a по y: ')),
                    int(input('Координата точки b по x: ')), int(input('Координата точки b по y: ')),
                    int(input('Координата точки c по x: ')), int(input('Координата точки c по y: ')))

print('Периметр треугольника:', triangle.perimeter())
print('Площадь треугольника:', triangle.area())
print('Точка пересечения медиан:', triangle.medianpoint())
