import matplotlib.pyplot as plt
from random import randint


def func(n):
    values = []
    for i in range(n):
        values.append(randint(1, 100))
    labels = range(1, n + 1)
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Круговая диаграмма из n рандомных частей")
    plt.show()


func(10)
