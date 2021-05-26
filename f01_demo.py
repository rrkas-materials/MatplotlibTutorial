from matplotlib import pyplot as plt
from f01_demo_data import *


if __name__ == '__main__':
    # plt.style.use('fivethirtyeight')
    # plt.style.use('ggplot')
    plt.xkcd()

    # plt.plot(ages_x, dev_y, 'k--', label='All Devs')
    # plt.plot(ages_x, py_dev_y, 'b', label='Python Devs')
    # plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.' ,label='All Devs')
    # plt.plot(ages_x, py_dev_y, color='b', marker='o' ,label='Python Devs')
    # plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python Devs')
    # plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JS Devs')
    plt.plot(ages_x, py_dev_y, label='Python Devs')
    plt.plot(ages_x, js_dev_y, label='JS Devs')
    plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')

    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.title('Median Salary (USD) by age')

    # plt.legend(['All Devs', 'Python Devs'])
    plt.legend()
    # plt.grid(True)
    # plt.tight_layout()

    plt.savefig('plots/plot02.png')

    plt.show()
