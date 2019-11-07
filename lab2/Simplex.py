import numpy as np
import matplotlib.pyplot as plt
from lab2.MyFunctions import MyFunctions

class Simplex:
    def __init__(self):
        self.__my_func = MyFunctions()

    def __create_x(self, x0, x1, x2):
        x = [0, 0]
        x[0] = -x0[0] + x1[0] + x2[0]
        x[1] = -x0[1] + x1[1] + x2[1]
        return x

    def __next_max(self, array):
        buff_array = array.copy()
        buff_array.sort(reverse=True)
        return buff_array[1]

    def SimplexSearch(self):
        plt.figure(2)
        count = 3

        e = 0.01
        accuracy = 2

        iteration = 0
        x_array = []

        alpha = 2

        delta_1 = ((np.sqrt(3) + 1) / (2 * np.sqrt(2))) * alpha
        delta_2 = ((np.sqrt(3) - 1) / (2 * np.sqrt(2))) * alpha

        x0 = [-2, 0]
        x1 = [x0[0] + delta_1, x0[1] + delta_2]
        x2 = [x0[0] + delta_2, x0[1] + delta_1]

        plt.annotate("x0", xy=(x0[0], x0[1]), xytext=(x0[0] - 1, x0[1] - 0.5))
        plt.annotate("x1", xy=(x1[0], x1[1]), xytext=(x1[0] - 1, x1[1] - 0.5))
        plt.annotate("x2", xy=(x2[0], x2[1]), xytext=(x2[0] - 1, x2[1] - 0.5))

        plt.plot(x0[0], x0[1], "ko")
        plt.plot(x1[0], x1[1], "ko")
        plt.plot(x2[0], x2[1], "ko")

        x_last = []

        f_s = [0, 0, 0]
        x_s = [x0, x1, x2]

        xes = [x_s[0][0], x_s[1][0], x_s[2][0], x_s[0][0]]
        yes = [x_s[0][1], x_s[1][1], x_s[2][1], x_s[0][1]]
        plt.plot(xes, yes, "b")

        while (True):
            f_s[0] = self.__my_func.f(x_s[0][0], x_s[0][1])
            f_s[1] = self.__my_func.f(x_s[1][0], x_s[1][1])
            f_s[2] = self.__my_func.f(x_s[2][0], x_s[2][1])

            xs = [x_s[0][0], x_s[1][0], x_s[2][0], x_s[0][0]]
            ys = [x_s[0][1], x_s[1][1], x_s[2][1], x_s[0][1]]
            plt.plot(xs, ys, "b")

            min_index = f_s.index(min(f_s))
            max_index = f_s.index(max(f_s))
            aver_index = f_s.index(self.__next_max(f_s))

            if (abs(f_s[max_index] - f_s[min_index]) < e):
                break

            if (x_array.__contains__(x_last)):
                iteration += 1
                if (iteration == accuracy):
                    break
                alpha = alpha / 2
                delta_1 = ((np.sqrt(3) + 1) / (2 * np.sqrt(2))) * alpha
                delta_2 = ((np.sqrt(3) - 1) / (2 * np.sqrt(2))) * alpha
                x_s[0] = [x_s[min_index][0], x_s[min_index][1]]
                x_s[1] = [x_s[0][0] + delta_1, x_s[0][1] + delta_2]
                x_s[2] = [x_s[0][0] + delta_2, x_s[0][1] + delta_1]
                x_array.clear()
                x_last = []
                continue

            x_array.append(x_last)

            if (x_s[max_index] != x_last):
                x_s[max_index] = self.__create_x(x_s[max_index], x_s[aver_index], x_s[min_index])
                x_last = x_s[max_index]
            else:
                x_s[aver_index] = self.__create_x(x_s[aver_index], x_s[max_index], x_s[min_index])
                x_last = x_s[aver_index]
            plt.plot(x_last[0], x_last[1], "ko")
            plt.annotate(f"x{count}", xy=(x_last[0], x_last[1]), xytext=(x_last[0] - 1, x_last[1] - 0.5))
            count += 1

        plt.plot(x_s[min_index][0], x_s[min_index][1], "ko", label=f"x_min = [{x_s[min_index][0]},{x_s[min_index][1]}]")

        print(f"Метод Cимплексного поиска: [{x_s[min_index][0]},{x_s[min_index][1]}]")

        plt.title("Метод симплексного поиска: " + r'$y=x1^2+x2^2; e=$' + str(e))
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y(x)$')
        plt.grid(True)
        plt.contour(self.__my_func.X(), self.__my_func.Y(), self.__my_func.Z(), [0, 20, 40, 60, 80, 100])
        plt.legend()




