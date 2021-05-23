from matplotlib import pyplot as plt
from f01_demo_data import *
import numpy as np

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')

    x_idx = np.arange(len(ages_x))
    width = 0.25

    plt.bar(x_idx - width, dev_y, width=width, color='#444444', linestyle='--', label='All Devs')
    # plt.plot(ages_x, py_dev_y, label='Python Devs')
    # plt.plot(ages_x, js_dev_y, label='JS Devs')
    plt.bar(x_idx, py_dev_y, width=width, label='Python Devs')
    plt.bar(x_idx + width, js_dev_y, width=width, label='JS Devs')

    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.xticks(ticks=x_idx, labels=ages_x)
    plt.title('Median Salary (USD) by age')

    plt.legend()
    plt.tight_layout()
    plt.show()
