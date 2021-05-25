import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')


    def animate(i):
        data = pd.read_csv('data/data11.csv')
        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']

        plt.cla()
        plt.plot(x, y1, label='Channel 1')
        plt.plot(x, y2, label='Channel 2')
        plt.legend(loc='upper left')
        plt.tight_layout()


    anim = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()
