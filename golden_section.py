import numpy as np


class GoldenSection():

    def __init__(self):
        self.PHI = (1 + np.sqrt(5)) / 2.0

    def f(self, x):
        f = np.power(x, 5) - np.power(x, 2)
        return f

    def findMin(self, a, b, e):
        k = 0
        while (True):
            x1 = b - (b - a) / self.PHI
            x2 = a + (b - a) / self.PHI
            k += 1
            if (self.f(x1) >= self.f(x2)):
                a = x1
            else:
                b = x2
            if (np.abs(b - a) < e):
                break
        print("Количество итераций {0}".format(k))
        return (a + b) / 2

    def findMax(self, a, b, e):
        while (True):
            x1 = b - (b - a) / self.PHI
            x2 = a + (b - a) / self.PHI
            if (self.f(x1) <= self.f(x2)):
                a = x1
            else:
                b = x2
            if (np.abs(b - a) < e):
                break
        return (a + b) / 2
