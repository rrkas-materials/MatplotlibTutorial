import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')

    # x_vals = [0, 1, 2, 3, 4, 5]
    # y_vals = [0, 1, 3, 2, 3, 5]
    x_vals = []
    y_vals = []

    plt.plot(x_vals, y_vals)

    index = count()


    def animate(i):
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 15))

        plt.cla()
        plt.plot(x_vals, y_vals)

    anim = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.tight_layout()
    plt.show()

