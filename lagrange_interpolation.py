from interpolation import Interpolation


class LagrangeInterpolation(Interpolation):
    def __call__(self, x):
        n = len(self.x)
        s = 0
        for i in range(n):
            denominator = 1
            numerator = 1
            # print(i)
            for j in range(n):
                if i != j:
                    # print(f'x({x}) - x{j}({self.x[j]}) = {x - self.x[j]}')
                    numerator *= x - self.x[j]
                    # print(f'x{i}({self.x[i]}) - x{j}({self.x[j]}) = {self.x[i] - self.x[j]}')
                    denominator *= self.x[i] - self.x[j]
            # print(numerator)
            # print(denominator)
            # print(numerator*denominator)
            s += numerator * self.y[self.x[i]] / denominator
        return s
