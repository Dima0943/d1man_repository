import matplotlib.pyplot as plt
from math import sin, cos


def func():
    x1 = [i / 10 for i in range(-120, 121)]
    x2 = [i / 10 for i in range(-120, 121)]
    x3 = [i / 10 for i in range(-120, 121)]
    x4 = [i / 10 for i in range(-120, 121)]
    y1 = [cos(x) for x in x1]
    y2 = [sin(x) for x in x2]
    y3 = [x ** 2 for x in x3]
    y4 = [2 / x if x != 0 else None for x in x4]
    plt.figure("4 функции", figsize=(12, 10))
    #
    plt.subplot(2, 2, 1)
    plt.plot(x1, y1)
    plt.title("y1=cos(x1)")
    plt.ylabel("y1")
    plt.xlabel("x1")
    plt.grid()
    #
    plt.subplot(2, 2, 2)
    plt.plot(x2, y2)
    plt.title("y2=sin(x2)")
    plt.ylabel("y2")
    plt.xlabel("x2")
    plt.grid()
    #
    plt.subplot(2, 2, 3)
    plt.plot(x3, y3)
    plt.title("y3=x3^2")
    plt.ylabel("y3")
    plt.xlabel("x3")
    plt.grid()
    #
    plt.subplot(2, 2, 4)
    plt.plot(x4, y4)
    plt.title("y4=2/x4")
    plt.ylabel("y4")
    plt.xlabel("x4")
    plt.grid()
    #
    plt.show()


func()
