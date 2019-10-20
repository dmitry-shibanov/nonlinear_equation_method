import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pylab
import math

def f(x):
    return x**5-x**2

def parab(a,b,c,x):
    return a*x**2+b*x+c


x_start = 0
x_end = 1
h = 0.01

e = 0.01

Xrange = np.arange(-1, 1.5, h)


def Approx(x1,x2,x3,f1,f2,f3):
    a0 = f1
    a1 = (f2-f1)/(x2-x1)
    a2 = (1/(x3-x2))*((f3-f1)/(x3-x1)-(f2-f1)/(x2-x1))
    x = ((x2+x1)/2) - (a1/(2*a2))
    
    r12=x1-x2
    r13=x1-x3
    r23=x2-x3
    s12=x1+x2
    s13=x1+x3
    s23=x2+x3
    p12=x1*x2
    p13=x1*x3
    p23=x2*x3

    a = (f1/(r12*r13)) - (f2/(r12*r23)) + (f3/(r13*r23))
    b = -((f1*s23)/(r12*r13)) + ((f2*s13)/(r12*r23)) - ((f3*s12)/(r13*r23))
    c = ((f1*p23)/(r12*r13)) - ((f2*p13)/(r12*r23)) + ((f3*p12)/(r13*r23))

    plt.plot(Xrange, parab(a,b,c,Xrange), ':')
    plt.plot(x, parab(a,b,c,x), 'bx')
    plt.plot(x, f(x), 'yo')

    return x

def Powell(x1,h,e):
    k=0
    Ymin=0.0
    Xmin=0.0
    x2=x1+h
    fx1=f(x1)
    fx2=f(x2)
    if fx1>fx2:
        x3=x1+2*h
    else:
        x3 = x1-h
    fx3=f(x3)
    k=k+3
    while(True):
        if(fx1<fx2 and fx1<fx3 ):
            Ymin = fx1
            Xmin = x1
        elif (fx2<fx1 and fx2<fx3):
            Ymin = fx2
            Xmin = x2
        elif (fx3<fx1 and fx3<fx2):
            Ymin = fx3
            Xmin = x3  
        x = Approx(x1,x2,x3,fx1,fx2,fx3)
        Yx = f(x)
        k = k + 1
        if(np.abs(Ymin-Yx)<=e and np.abs(Xmin-x)<=e):
            break
        if(fx1>fx2 and fx1>fx3 and fx1>Yx):
            x1 = x
            fx1 = Yx
        elif(fx2>fx1 and fx2>fx3 and fx2>Yx):
            x2 = x
            fx2 = Yx
        elif(fx3>fx1 and fx3>fx2 and fx3>Yx):
            x3 = x
            fx3 = Yx
    return x, k



x1 = 2 # начальная точка расчетов
h = 0.1 # дельта

x_min_2, count_powell = Powell(x1,h,e)
print("Количество итераций {0} точка x = {1}".format(x_min_2,count_powell))

plt.figure(1)
plt.title("Метод Пауэлла")
plt.ylim(-0.4,1)
plt.xlabel(r'$x$') #Метка по оси x в формате TeX
plt.ylabel(r'$y(x)$') #Метка по оси y в формате TeX
plt.grid(True) #Сетка
plt.plot(Xrange,f(Xrange), '') # Основная функция
#plt.plot(x_min_2, f(x_min_2), 'bo', label="минимальное  = " + x_min_2.__str__())
plt.legend()
#
# plt.figure(2)
# plt.xlabel(r'$x$') #Метка по оси x в формате TeX
# plt.ylabel(r'$y(x)$') #Метка по оси y в формате TeX
# plt.title("Golden method: " + r'$y=x^3-x; e=$' + e.__str__())
# plt.grid(True) #Сетка
#
# plt.plot(Xrange,f(Xrange), '') # Основная функция
# plt.plot(x_min_1, f(x_min_1), 'bo', label="Xmin = " + x_min_1.__str__())
#
# plt.annotate("x_min", xy=(x_min_1,f(x_min_1)), xytext=(x_min_1,f(x_min_1) + 1), arrowprops=dict(facecolor='black', shrink=0.09))
# plt.legend()
#
# plt.figure(3)
# plt.xlabel(r'$x$') #Метка по оси x в формате TeX
# plt.ylabel(r'$y(x)$') #Метка по оси y в формате TeX
# plt.title("Half method: " + r'$y=x^3-x; e=$' + e.__str__())
# plt.grid(True) #Сетка
#
# plt.plot(Xrange,f(Xrange), '') # Основная функция
# plt.plot(x_min_3, f(x_min_3), 'bo', label="Xmin = " + x_min_3.__str__())
#
# plt.legend()

#plt.figure(3)
#plt.xlabel(r'$x$') #Метка по оси x в формате TeX
#plt.ylabel(r'$y(x)$') #Метка по оси y в формате TeX
#plt.title(r'$y=x^3-x; x ∈ [0,1]$')
#plt.grid(True)
#plt.plot(Xrange,f(Xrange),'')


plt.show() #Показать график