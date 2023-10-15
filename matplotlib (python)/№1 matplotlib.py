import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def func(a, b):
    f1 = a.split('=')[1]
    f2 = b.split('=')[1]
    x = [i for i in range(-50, 51)]
    y1 = [eval(f1) for x in x]
    y2 = [eval(f2) for x in x]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f"Зависимости: {a}, {b}", fontsize=16)
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("y1, y2", fontsize=14)
    ax.grid(which="major", linewidth=1.2)
    ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
    ax.plot(x, y1, label=a)
    ax.plot(x, y2, label=b)
    ax.legend()
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)
    plt.show()

# формат вызова функции: func('y1=2*x+5', 'y2=-x-1')
