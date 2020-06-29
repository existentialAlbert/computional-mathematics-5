import pandas as pd

from lagrange_interpolation import LagrangeInterpolation
from linear_interpolation import LinearInterpolation
from newton_interpolation import NewtonInterpolation
from quadratic_interpolation import QuadraticInterpolation

if __name__ == "__main__":
    while True:
        try:
            print('Выберите таблицу 1 или 2')
            number_of_table = input()
            table = pd.read_csv(f'./table{number_of_table}.csv', sep=' ')
            if number_of_table != '1' and number_of_table != '2':
                print('Сказано же, 1 или 2! Попробуйте еще раз')
                continue
            x = table['x'].values
            y = table['y'].values
            print(f'x = {x}')
            print(f'y = {y}')
            # x = [0.593, 0.598, 0.605, 0.613, 0.619, 0.627, 0.632]
            # y = [0.532, 0.5356, 0.5406, 0.5462, 0.5504, 0.5559, 0.5594]
            # x = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
            # y = [1.5320, 2.5356, 3.5406, 4.5462, 5.5504, 6.5559, 7.5594]
            print('Введите значение:')
            _x = 0
            while True:
                _x = float(input())
                if _x < x[0] or _x > x[-1]:
                    print('Введите икс в пределах одз!')
                else:
                    break
            print("Линейная интерполяция: ")
            interpolator = LinearInterpolation(x, y)
            print(round(interpolator(_x), 5))
            print("Квадратичное интерполяция: ")

            interpolator = QuadraticInterpolation(x, y)
            print(round(interpolator(_x), 5))
            print("Интерполяция методом Лагранжа: ")

            interpolator = LagrangeInterpolation(x, y)
            print(round(interpolator(_x), 5))
            print("Интерполяция методом Ньютона: ")

            interpolator = NewtonInterpolation(x, y)
            print(round(interpolator(_x), 5))

        except BaseException as e:
            print(e.args[0])
