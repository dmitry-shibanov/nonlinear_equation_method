from builtins import float, input
import numpy as np
import matplotlib.pyplot as plt
from golden_section import GoldenSection

# Золотое сечение
print('Введите начальное значение x = ')
start = float(input())
print('Введите конечное значение x = ')
end = float(input())
print('Введите точность е = ')
e = float(input())

t1 = np.arange(start - 3, end + 3, 0.1)
golden_method = GoldenSection()
min = golden_method.findMin(start, end, e)
print('Минимальное значение при x = {0} и y = {1}'.format(min,golden_method.f(min)))


# Метод Ньютона




# Метод половинного деления





figure, ax = plt.subplots()
ax.grid()
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# 'bo'
ax.plot(t1, golden_method.f(t1), '-', min, golden_method.f(min), 'bo')
ax.set(xlabel='X', ylabel='F(x)',
       title='Золотое сечение')
plt.show()
