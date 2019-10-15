import numpy as np


class NutonMethod:
    def findMin(self, a, b, e):
        try:
            x0 = (a + b) / 2
            xn = self.f(x0)
            xn1 = xn - self.f(xn) / self.f1(xn)
            while np.abs(xn1 - xn) > e:
                xn = xn1
                xn1 = xn - self.f(xn) / self.f1(xn)
            return xn1
        except ValueError:
            print("Value not invalidate")

    def findMax(self, a, b, e):
        return ''

    def f(self, x):
        f = np.power(x, 5) - np.power(x, 2)
        return f

    def f1(self, x):
        f = 5 * np.power(x, 4) - 2 * x
        return f
