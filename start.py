from builtins import float, input
import numpy as np
import matplotlib.pyplot as plt
from golden_section import GoldenSection
from halving_method import HalvingMethod
from method_paul import PaulMethod

# t = np.arange(3, 3, 0.1)

def f(x):
    f_x = np.power(x,5) - np.power(x,2)
    return f_x

def show_f():
    plt.figure(2)
    font = {'size': 7}
    plt.rc('font', **font)
    plt.title("Функция")
    plt.ylim(-0.4, 1)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y(x)$')
    plt.grid(True)  # Сетка
    X = np.arange(-0.5,1.5,0.05)
    plt.plot(X, f(X), label="f(x) = x^5 - x^2")  # Основная функция
    plt.legend()

    plt.show()


def graph(t1, f, min, methodName):
    figure, ax = plt.subplots()
    figure.suptitle("x = {0} y = {1}".format(min, f(min)))
    ax.grid()
    ax.plot(t1, f(t1), '-', min, f(min), 'bo')
    ax.set(xlabel=r'$x$', ylabel=r'$y(x)$',
           title=methodName, )

    plt.show()


print('Введите начальное значение x = ')
start = float(input())
print('Введите конечное значение x = ')
end = float(input())
print('Введите точность е = ')
e = float(input())

t1 = np.arange(start - 3, end + 3, 0.1)

# Сама функция

# show_f()


# метод Золотого деления

# golden_method = GoldenSection()
# min = golden_method.findMin(start, end, e)
# print('Минимальное значение при x = {0} и y = {1}'.format(min, golden_method.f(min)))
#
# graph(t1, golden_method.f, min, "Золотое сечение")


# Метод Пауэлла

paul_method = PaulMethod(0.01)
x_min, count_powell = paul_method.Powell(1, 0.1, e)
paul_method.show()
print('Минимальное значение при x = {0} и y = {1}'.format(x_min, paul_method.f(x_min)))
print('Количество итераций {0}'.format(11))


# Метод половинного деления
#
# paul_method = HalvingMethod()
# min = paul_method.findMin(start,end,e)
# print('Минимальное значение при x = {0} и y = {1}'.format(min, paul_method.f(min)))
# graph(t1, paul_method.f, min, "метод половинного деления")
