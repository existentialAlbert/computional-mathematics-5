from abc import abstractmethod


class Interpolation:
    def __init__(self, x, y):
        self.y = {}
        self.x = x
        for i in range(len(x)):
            self.y[x[i]] = y[i]
        self.x.sort()

    @abstractmethod
    def __call__(self, x):
        pass

    def find_interval(self, x):
        index = 0
        while x > self.x[index]:
            index += 1
        return self.x[index - 1], self.x[index]
