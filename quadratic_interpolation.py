from interpolation import Interpolation
import numpy as np


class QuadraticInterpolation(Interpolation):
    def find_interval(self, x):
        for i in range(1, len(self.x) - 1):
            x0 = self.x[i - 1]
            x1 = self.x[i]
            x2 = self.x[i + 1]
            interval = lambda x: x2 >= x >= x0
            if interval(x):
                return x0, x1, x2

    def __call__(self, x):
        x0, x1, x2 = self.find_interval(x)
        y0 = self.y[x0]
        y1 = self.y[x1]
        y2 = self.y[x2]
        matrix = np.array([[x0 ** 2, x0, 1, y0],
                           [x1 ** 2, x1, 1, y1],
                           [x2 ** 2, x2, 1, y2]])
        a, b, c = self.__solve_linear_system(matrix)
        f = lambda x: a * x ** 2 + b * x + c
        return f(x)

    @staticmethod
    def __solve_linear_system(matrix: np.array):
        det = np.linalg.det(matrix[:, :-1])
        if det != 0:
            det_1 = np.linalg.det(matrix[:, [3, 1, 2]])
            det_2 = np.linalg.det(matrix[:, [0, 3, 2]])
            det_3 = np.linalg.det(matrix[:, [0, 1, 3]])
            return det_1 / det, det_2 / det, det_3 / det
        raise ZeroDivisionError('Интерполяция на данном участке невозможна!')
