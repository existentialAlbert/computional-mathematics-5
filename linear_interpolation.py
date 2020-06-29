from interpolation import Interpolation


class LinearInterpolation(Interpolation):
    def __call__(self, x):
        x0, x1 = self.find_interval(x)
        y0 = self.y[x0]
        y1 = self.y[x1]
        k = (y1 - y0) / (x1 - x0)
        b = y0 - k * x0
        f = lambda x: k * x + b
        return f(x)
