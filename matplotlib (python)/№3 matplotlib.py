import matplotlib.pyplot as plt
from random import randint


def func():
    counts = []
    for _ in range(7):
        counts.append(randint(0, 100))
    nums = range(1, 8)
    plt.bar(nums, counts)
    plt.title("Столбчатый график из 7 столбцов")
    plt.xlabel("Столбец")
    plt.ylabel("Значение")
    plt.grid()
    plt.show()


func()
