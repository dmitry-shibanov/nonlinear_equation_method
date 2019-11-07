import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pylab
import math


def f2(x1, x2):
    return (x1 - 6) ** 2 + (x2 - 1) ** 2 + x1 * x2


def f(x1, x2):
    return (1 - x1) ** 2 + 100 * (x2 - x1 ** 2) ** 2


def f2(x1, x2):
    return (x1 - 2) ** 2 + (x2 - 9) ** 2 + x1 * x2


Xrange = np.arange(-5, 5, 0.01)
Yrange = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(Xrange, Yrange)
Z = f(X, Y)

plt.figure(3)
plt.title(r'$y=x1^2+x2^2$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.grid(True)
plt.contour(X, Y, Z, [0, 10, 20, 30, 40, 50])


def HookJeves():
    def Obrazec(x_base, x_last_base):
        x1 = x_base[0] + (x_base[0] - x_last_base[0])
        x2 = x_base[1] + (x_base[1] - x_last_base[1])
        return [x1, x2]

    def Search(x_base):
        fx0 = f(x_base[0], x_base[1])
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
            f_s[i] = f(x_s[i][0], x_s[i][1])

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

    fx0 = f(x_base[0], x_base[1])
    x_new = Search(x_base)

    while (True):
        fk = f(x_base[0], x_base[1])
        fk1 = f(x_new[0], x_new[1])
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
            plt.annotate(f"x{count}", xy=(x_last_base[0], x_last_base[1]), xytext=(x_last_base[0], x_last_base[1] - 1))
            plt.plot(x_es, y_es, 'b')
        else:
            dx = math.sqrt(h[0] ** 2 + h[1] ** 2)
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
    plt.contour(X, Y, Z, [0, 20, 40, 60, 80, 100])
    plt.legend()


def SimplexSearch():
    def new_x(x0, x1, x2):
        x = [0, 0]
        x[0] = -x0[0] + x1[0] + x2[0]
        x[1] = -x0[1] + x1[1] + x2[1]
        return x

    def next_after_max(array):
        buff_array = array.copy()
        buff_array.sort(reverse=True)
        return buff_array[1]

    plt.figure(2)
    count = 3

    e = 0.01
    accuracy = 2

    iteration = 0
    x_array = []

    alpha = 2

    delta_1 = ((math.sqrt(3) + 1) / (2 * math.sqrt(2))) * alpha
    delta_2 = ((math.sqrt(3) - 1) / (2 * math.sqrt(2))) * alpha

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
        f_s[0] = f(x_s[0][0], x_s[0][1])
        f_s[1] = f(x_s[1][0], x_s[1][1])
        f_s[2] = f(x_s[2][0], x_s[2][1])

        xs = [x_s[0][0], x_s[1][0], x_s[2][0], x_s[0][0]]
        ys = [x_s[0][1], x_s[1][1], x_s[2][1], x_s[0][1]]
        plt.plot(xs, ys, "b")

        min_index = f_s.index(min(f_s))
        max_index = f_s.index(max(f_s))
        aver_index = f_s.index(next_after_max(f_s))

        if (abs(f_s[max_index] - f_s[min_index]) < e):
            break

        if (x_array.__contains__(x_last)):
            iteration += 1
            if (iteration == accuracy):
                break
            alpha = alpha / 2
            delta_1 = ((math.sqrt(3) + 1) / (2 * math.sqrt(2))) * alpha
            delta_2 = ((math.sqrt(3) - 1) / (2 * math.sqrt(2))) * alpha
            x_s[0] = [x_s[min_index][0], x_s[min_index][1]]
            x_s[1] = [x_s[0][0] + delta_1, x_s[0][1] + delta_2]
            x_s[2] = [x_s[0][0] + delta_2, x_s[0][1] + delta_1]
            x_array.clear()
            x_last = []
            continue

        x_array.append(x_last)

        if (x_s[max_index] != x_last):
            x_s[max_index] = new_x(x_s[max_index], x_s[aver_index], x_s[min_index])
            x_last = x_s[max_index]
        else:
            x_s[aver_index] = new_x(x_s[aver_index], x_s[max_index], x_s[min_index])
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
    plt.contour(X, Y, Z, [0, 20, 40, 60, 80, 100])
    plt.legend()


HookJeves()
SimplexSearch()

plt.show()