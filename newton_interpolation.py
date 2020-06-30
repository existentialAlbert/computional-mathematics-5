from interpolation import Interpolation
import pandas as pd
import numpy as np

from unequal_spaced_steps_newton_interpolation import UneqSpacedNewtonInterpolation


class NewtonInterpolation(Interpolation):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.begin = 0
        self.uneq = UneqSpacedNewtonInterpolation(x, y)
        self.n = len(self.x)

    def __call__(self, x_):
        x = self.x
        h = round(x[1] - x[0], 8)
        a = x[0]
        for i in self.x[1:]:
            if round(i - a, 8) != h:  # если неравноотстоящие, то вычисляем по другой формуле
                return self.uneq(x_)
            a = i
        self.begin = 0
        while x_ > self.x[self.begin]:
            self.begin += 1
        if self.begin <= len(self.x) // 2:  # если левая половина массива, то берем левую границу интервала
            self.begin -= 1
        res = None
        t = (x_ - x[self.begin]) / h
        # print(x[self.begin])
        if self.begin <= self.n // 2:
            res = self.forwards(t)
        elif self.begin >= self.n // 2:
            res = self.backwards(t)
        return res

    def forwards(self, t):
        """
        Вычисление формулой вперед
        :param t:
        :return:
        """
        res = self.y[self.x[self.begin]] + t * self.delta(1)
        ti = t
        j = 1
        for i in range(self.begin + 1, self.n - 1):
            ti *= t - j
            res += ti * self.delta(j + 1) / self.__factorial(j + 1)
            j += 1
        return res

    def backwards(self, t):
        """
        Вычисление формулой назад
        :param t:
        :return:
        """
        res = self.y[self.x[self.begin]] + t * self.delta(1, self.begin - 1)
        ti = t
        for i in range(1, self.begin):
            ti *= t + i
            d = self.delta(i + 1, self.begin - i - 1)
            res += ti / self.__factorial(i + 1) * d
        return res

    def delta(self, q, p=None):
        """
        С помощью этого метода берем определенную ячейку в таблице
        :param: p - i
        :param: q - порядок
        """
        if p is None:
            p = self.begin
        return self.calc_current_delta(q)[p]

    def calc_current_delta(self, q):
        """
        Метод вычисляет ряд q-го порядка
        :param q: порядок разделенной разности
        :return:
        """
        res = [np.nan for i in range(self.n)]
        if q == 1:
            for i in range(self.n - 1):
                res[i] = self.y[self.x[1 + i]] - self.y[self.x[i]]
        else:
            for i in range(self.n - 1):
                c = self.calc_current_delta(q - 1)
                b = c[i]
                a = c[i + 1]
                res[i] = round(a - b, 5)
        return res

    def __factorial(self, n):
        return n * self.__factorial(n - 1) if n > 1 else 1

    def print_table(self):
        rows = []
        index = ['∆y_i', '∆^2 y_i', '∆^3 y_i', '∆^4 y_i', '∆^5 y_i', '∆^6 y_i']
        for i in range(1, self.n):
            rows.append(self.calc_current_delta(i)[:-1])
        table = pd.DataFrame(rows, index=index)
        print(table)

    def get_table(self):
        rows = []
        for i in range(1, self.n):
            rows.append(self.calc_current_delta(i)[:-1])
        return rows
