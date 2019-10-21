import numpy as np
import matplotlib.pyplot as plt


class PaulMethod:

    def f(self, x):
        return x ** 5 - x ** 2

    def parabal(self, a, b, c, x):
        return a * x ** 2 + b * x + c

    def __init__(self, h):
        self.h = 0.01
        self.Xrange = np.arange(-1, 1.5, h)

    def Approx(self, x1, x2, x3, f1, f2, f3):
        a0 = f1
        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1))
        x = ((x2 + x1) / 2) - (a1 / (2 * a2))

        r12 = x1 - x2
        r13 = x1 - x3
        r23 = x2 - x3
        s12 = x1 + x2
        s13 = x1 + x3
        s23 = x2 + x3
        p12 = x1 * x2
        p13 = x1 * x3
        p23 = x2 * x3

        a = (f1 / (r12 * r13)) - (f2 / (r12 * r23)) + (f3 / (r13 * r23))
        b = -((f1 * s23) / (r12 * r13)) + ((f2 * s13) / (r12 * r23)) - ((f3 * s12) / (r13 * r23))
        c = ((f1 * p23) / (r12 * r13)) - ((f2 * p13) / (r12 * r23)) + ((f3 * p12) / (r13 * r23))

        plt.plot(self.Xrange, self.parabal(a, b, c, self.Xrange), ':',
                 label="{0}*x^2 + {1}*x + {2}".format(round(a, 2), round(b, 2), round(c, 2)))
        plt.plot(x, self.parabal(a, b, c, x), 'bx',
                 label="x = {0} y = {1}".format(round(x, 2), round(self.parabal(a, b, c, x), 2)))
        plt.plot(x, self.f(x), 'yo', label="x = {0} y = {1}".format(round(x, 2), round(self.f(x), 2)))

        return x

    def Powell(self, x1, h, e):
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
            x = self.Approx(x1, x2, x3, fx1, fx2, fx3)
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
        return x, k

    def show(self):
        plt.figure(1)
        font = {'size': 7}
        plt.rc('font', **font)
        plt.title("Метод Пауэлла")
        plt.ylim(-0.4, 1)
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y(x)$')
        plt.grid(True)  # Сетка
        plt.plot(self.Xrange, self.f(self.Xrange), label="f(x) = x^5 - x^2")  # Основная функция
        plt.legend()

        plt.show()  # Показать график
