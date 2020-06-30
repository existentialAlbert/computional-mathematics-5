from interpolation import Interpolation


class UneqSpacedNewtonInterpolation(Interpolation):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dif_x = []
        self.dif_y = []

    def __call__(self, x):
        res = 0
        n = len(self.x) - 1  # указывает на последний элемент
        for i in range(1, n):
            if self.x[n] > x > self.x[n - 1] or x > self.x[i] and n - i < 3:
                for j in range(1, -1, -1):
                    self.dif_x = [self.x[n - 2 - j], self.x[n - 1 - j], self.x[n - j]]
                    self.dif_y = [self.y[self.x[n - 2 - j]], self.y[self.x[n - 1 - j]],
                                  self.y[self.x[n - j]]]
                    res += self.calculate(x)
                break
            elif self.x[0] < x < self.x[1] or x > self.x[i] and n - i >= 3:
                for j in range(2):
                    self.dif_x = [self.x[i + j - 1], self.x[i + j], self.x[i + j + 1]]
                    self.dif_y = [self.y[self.x[i + j - 1]], self.y[self.x[i + j]],
                                  self.y[self.x[i + j + 1]]]
                    res += self.calculate(x)
                break
        return res / 2

    def calculate(self, x):
        """
        Вычисляет значение интерполяционного многочлена Ньютона до 3 порядка
        :param x:
        :return:
        """
        return self.dif_y[0] + self.diff_1(0, 1) * (x - self.dif_x[0]) + self.diff_2(0, 1, 2) * (
                x - self.dif_x[0]) * (
                       x - self.dif_x[1])

    def diff_1(self, a, b):
        """
        Вычисляет разность 1 порядка
        :param a:
        :param b:
        :return:
        """
        return (self.dif_y[b] - self.dif_y[a]) / (self.dif_x[b] - self.dif_x[a])

    def diff_2(self, a, b, c):
        """
        Вычисляет разность 2 порядка
        :param a:
        :param b:
        :param c:
        :return:
        """
        return (self.diff_1(b, c) - self.diff_1(a, b)) / (self.dif_x[c] - self.dif_x[a])
