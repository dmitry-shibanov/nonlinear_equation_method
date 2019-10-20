import numpy as np


class HalvingMethod:

    def findMin(self, a, b, e):
        k = 0
        xm = (a + b) / 2
        L = b - a
        yxm = self.f(xm)
        # k = k + 1
        while L > e:
            x1 = a + L / 4
            x2 = b - L / 4
            yx1 = self.f(x1)
            yx2 = self.f(x2)
            k = k + 2
            if (yx1 < yxm):
                b = xm
                xm = x1
                yxm = yx1
            elif (yx2 < yxm):
                a = xm
                xm = x2
                yxm = yx2
            else:
                a = x1
                b = x2
            L = b - a
        print("Количество итераций по циклу метода дихатомии {0}".format(k))
        return xm

    def f(self, x):
        f = np.power(x, 5) - np.power(x, 2)
        return f




        # while abs(b - a) > e:
        #     x = (a + b) / 2.0
        #     fx = self.f(x)
        #     fa = self.f(a)
        #     if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
        #         a = x
        #     else:
        #         b = x
        # return x