from builtins import float, input
import numpy as np
import matplotlib.pyplot as plt
from golden_section import GoldenSection
from halving_method import HalvingMethod
from method_paul import PaulMethod

t = np.arange(3, 3, 0.1)

def Approx(x1, x2, x3, f1, f2, f3,f):
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

    plt.plot(t, parabals(a, b, c, t), ':')
    plt.plot(x, parabals(a, b, c, x), 'bx')
    plt.plot(x, f(x), 'yo')

    return x

def parabals(a,b,c,x):
    return a*x**2+b*x+c

def graph(t1, f, min, methodName):
    figure, ax = plt.subplots()
    ax.grid()
    # plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    # 'bo'
    ax.plot(t1, f(t1), '-', min, f(min), 'bo')
    ax.set(xlabel='X', ylabel='F(x)',
           title=methodName)
    plt.show()


# Золотое сечение
print('Введите начальное значение x = ')
start = float(input())
print('Введите конечное значение x = ')
end = float(input())
print('Введите точность е = ')
e = float(input())

t1 = np.arange(start - 3, end + 3, 0.1)
# golden_method = GoldenSection()
# min = golden_method.findMin(start, end, e)
# print('Минимальное значение при x = {0} и y = {1}'.format(min, golden_method.f(min)))
#
# graph(t1, golden_method.f, min, "Золотое сечение")


# Метод Пауэлла

# paul_method = PaulMethod()
# min = paul_method.findMin(2,0.1,e,Approx)
# plt.figure(1)
# plt.title("Метод Пауэлла")
# plt.ylim(-0.4,1)
# plt.xlabel(r'$x$') #Метка по оси x в формате TeX
# plt.ylabel(r'$y(x)$') #Метка по оси y в формате TeX
# plt.grid(True) #Сетка
# plt.plot(t1,paul_method.f(t1), '') # Основная функция
# plt.plot(min, paul_method.f(min), 'bo', label="Xmin = " + min.__str__())
# plt.legend()

# print('Минимальное значение при x = {0} и y = {1}'.format(min, paul_method.f(min)))
# graph(t1, paul_method.f, min, "метод Пауэлла")

# Метод половинного деления
#
# paul_method = HalvingMethod()
# min = paul_method.findMin(start,end,e)
# print('Минимальное значение при x = {0} и y = {1}'.format(min, paul_method.f(min)))
# graph(t1, paul_method.f, min, "метод половинного деления")

# 0.7745418341969438

# plt.show()