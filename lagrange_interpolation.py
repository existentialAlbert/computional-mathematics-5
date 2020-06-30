from interpolation import Interpolation


class LagrangeInterpolation(Interpolation):
    def __call__(self, x):
        n = len(self.x)
        s = 0
        for i in range(n):
            denominator = 1
            numerator = 1
            for j in range(n):
                if i != j:
                    numerator *= x - self.x[j]
                    denominator *= self.x[i] - self.x[j]
            s += numerator * self.y[self.x[i]] / denominator
        return s
