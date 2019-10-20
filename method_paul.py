import numpy as np


class PaulMethod:

    # def findMin(self, a, b, e):
    def findMin(self, x1, h, e, Approx):
        k = 0
        Ymin = 0.0
        Xmin = 0.0
        x2 = x1 + h
        fx1 = self.f(x1)
        fx2 = self.f(x2)
        if fx1 > fx2:
            x3 = x1 + 2 * h
        else:
            x3 = x1 - h
        fx3 = self.f(x3)
        k = k + 3
        while (True):
            if (fx1 < fx2 and fx1 < fx3):
                Ymin = fx1
                Xmin = x1
            elif (fx2 < fx1 and fx2 < fx3):
                Ymin = fx2
                Xmin = x2
            elif (fx3 < fx1 and fx3 < fx2):
                Ymin = fx3
                Xmin = x3
            x = Approx(x1, x2, x3, fx1, fx2, fx3, self.f)
            Yx = self.f(x)
            k = k + 1
            if (np.abs(Ymin - Yx) <= e and np.abs(Xmin - x) <= e):
                break
            if (fx1 > fx2 and fx1 > fx3 and fx1 > Yx):
                x1 = x
                fx1 = Yx
            elif (fx2 > fx1 and fx2 > fx3 and fx2 > Yx):
                x2 = x
                fx2 = Yx
            elif (fx3 > fx1 and fx3 > fx2 and fx3 > Yx):
                x3 = x
                fx3 = Yx
        print(k)
        return x

    def f(self, x):
        f = np.power(x, 5) - np.power(x, 2)
        return f





        # h = 0.01
        # e2 = 0.1
        # x1 = a
        # Xmin = 0
        # x2 = x1 + h
        # fx1 = self.f(x1)
        # fx2 = self.f(x2)
        # if fx1 > fx2:
        #     self.x3 = x1 + 2 * h
        # else:
        #     self.x3 = x1 - h
        # while True:
        #     fx3 = self.f(self.x3)
        #     arrayX = [x1, x2, self.x3]
        #     arrayF = [fx1, fx2, fx3]
        #     FminIndex = np.argmin(arrayF)
        #     Xmin = arrayX[FminIndex]
        #     Fmin = arrayF[FminIndex]
        #     a1 = (fx2 - fx1) / (x2 - x1)
        #     a2 = 1 / (self.x3 - x2) * ((fx3 - fx1) / (self.x3 - x1) - (fx2 - fx1) / (x2 - x1))
        #     x = (x2 + x1) / 2.0 - a1 / (2 * a2)
        #     if np.abs(Fmin - self.f(x)) < e: #and np.abs(Fmin - self.f(x)) < e2
        #         break
        #     else:
        #         if Fmin > self.f(x):
        #             x2 = x
        #         else:
        #             x2 = Xmin
        #
        #         x1 = x2 - (b - x2) / 200.0
        #         self.x3 = x2 + (b - x2) / 200.0
        #         print('Минимальное значение при xmin = {0} и x = {1}'.format(Xmin, x))
        #         print("x1 = {0} и x2 = {1} и x3 = {2}".format(x1, x2, self.x3))
        # return Xmin