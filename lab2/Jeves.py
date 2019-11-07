import numpy as np
import matplotlib.pyplot as plt
from lab2.MyFunctions import MyFunctions

class Jeves:

    def __init__(self):
        self.__my_func = MyFunctions()

    def HookJeves(self):
        def Obrazec(x_base, x_last_base):
            x1 = x_base[0] + (x_base[0] - x_last_base[0])
            x2 = x_base[1] + (x_base[1] - x_last_base[1])
            return [x1, x2]

        def Search(x_base):
            fx0 = self.__my_func.f(x_base[0], x_base[1])
            x_new = [x_base[0], x_base[1]]

            x_s = [0, 0, 0, 0, 0, 0, 0, 0]

            x_s[0] = [x_base[0] + h[0], x_base[1]]
            x_s[1] = [x_base[0] + h[0], x_base[1] + h[1]]
            x_s[2] = [x_base[0] + h[0], x_base[1] - h[1]]
            x_s[3] = [x_base[0], x_base[1] + h[1]]
            x_s[4] = [x_base[0], x_base[1] - h[1]]
            x_s[5] = [x_base[0] - h[0], x_base[1]]
            x_s[6] = [x_base[0] - h[0], x_base[1] + h[1]]
            x_s[7] = [x_base[0] - h[0], x_base[1] - h[1]]

            f_s = [0, 0, 0, 0, 0, 0, 0, 0]

            for i in range(8):
                f_s[i] = self.__my_func.f(x_s[i][0], x_s[i][1])

            min_index = f_s.index(min(f_s))

            if (f_s[min_index] < fx0):
                x_new[0] = x_s[min_index][0]
                x_new[1] = x_s[min_index][1]

            return x_new

        plt.figure(1)
        count = 0

        x_base = [-1, 1]
        h = [1, 1]
        e = 0.01
        a = 2

        x_last_base = [0, 0]

        fx0 = self.__my_func.f(x_base[0], x_base[1])
        x_new = Search(x_base)

        while (True):
            fk = self.__my_func.f(x_base[0], x_base[1])
            fk1 = self.__my_func.f(x_new[0], x_new[1])
            if (fk1 < fk):
                x_last_base[0] = x_base[0]
                x_last_base[1] = x_base[1]
                x_base[0] = x_new[0]
                x_base[1] = x_new[1]
                x_new = Obrazec(x_base, x_last_base)
                x_new = Search(x_new)

                count += 1
                x_es = [x_last_base[0], x_base[0]]
                y_es = [x_last_base[1], x_base[1]]
                plt.plot(x_last_base[0], x_last_base[1], 'ko')
                plt.annotate(f"x{count}", xy=(x_last_base[0], x_last_base[1]),
                             xytext=(x_last_base[0], x_last_base[1] - 1))
                plt.plot(x_es, y_es, 'b')
            else:
                dx = np.sqrt(h[0] ** 2 + h[1] ** 2)
                if (dx < e):
                    plt.plot(x_base[0], x_base[1], 'ko', label=f"x_min = [{x_base[0]},{x_base[1]}]")
                    plt.annotate(f"x{count + 1}", xy=(x_base[0], x_base[1]), xytext=(x_base[0], x_base[1] - 1))
                    break
                else:
                    h[0] = h[0] / a
                    h[1] = h[1] / a
                    x_new = Search(x_base)

        print(f"Метод Хука-Дживса: [{x_base[0]},{x_base[1]}]")

        plt.title("Метод Хука-Дживса: " + r'$y=x1^2+x2^2; e=$' + str(e))
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y(x)$')
        plt.grid(True)
        plt.contour(self.__my_func.X, self.__my_func.Y, self.__my_func.Z, [0, 20, 40, 60, 80, 100])
        plt.legend()
