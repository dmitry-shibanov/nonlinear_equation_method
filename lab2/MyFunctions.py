import numpy as np
import matplotlib.pyplot as plt
import math

class MyFunctions:

    def __init__(self):
        self.__x_range = np.arange(-5, 5, 0.01)
        self.__y_range = np.arange(-5, 5, 0.01)
        self.__X, self.__Y = np.meshgrid(self.__x_range, self.__y_range)

    def f0(self, x1, x2):
        return np.power(x1 - 6, 2) + np.power(x2 - 1, 2) + x1 * x2

    def f(self, x1, x2):
        return (1 - x1) ** 2 + 100 * (x2 - x1 ** 2) ** 2
        # return np.power(1 - x1, 2) + 100 * np.power(x2 - x1**2, 2)

    def f2(self, x1, x2):
        return np.power(x1 - 2, 2) + np.power(x2 - 9, 2) + x1 * x2

    def getXRande(self):
        return self.__x_range

    def getYRange(self):
        return self.__y_range

    def X(self):
        return self.__X

    def Y(self):
        return self.__Y

    def Z(self):
        return self.f(self.__X, self.__Y)

    def figure(self):
        plt.figure(3)
        plt.title(r'$y=x1^2+x2^2$')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y(x)$')
        plt.grid(True)
        print(self.Z())
        plt.contour(self.__X, self.__Y, self.Z(), [0, 10, 20, 30, 40, 50])
