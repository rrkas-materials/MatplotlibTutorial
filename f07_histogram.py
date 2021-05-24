import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')

    # ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

    data = pd.read_csv('data/data07.csv')
    ids = data['Responder_id']
    ages = data['Age']
    bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    median_age = 29
    color = '#fc4f30'

    plt.hist(ages, bins=bins, edgecolor='black', log=True)
    plt.axvline(x=29, color=color, label='Age Median', linewidth=2)
    plt.legend()

    plt.title('Ages of Respondents')
    plt.xlabel('Ages')
    plt.ylabel('Total Respondents')

    plt.tight_layout()

    plt.show()
