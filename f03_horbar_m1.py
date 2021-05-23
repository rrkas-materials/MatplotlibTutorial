from matplotlib import pyplot as plt
import csv
from collections import Counter

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')

    with open('data/data03.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        c = Counter()

        for row in csv_reader:
            c.update(row['LanguagesWorkedWith'].split(';'))

    # print(c.most_common(15))


    languages = []
    freq = []

    # method 1
    # for item in c.most_common(15):
    #     languages.append(item[0])
    #     freq.append(item[1])

    # method 2
    for l, f in c.most_common(15):
        languages.append(l)
        freq.append(f)


    languages.reverse()
    freq.reverse()

    plt.barh(languages, freq, label='Python Devs')
    # plt.ylabel('Language')
    plt.xlabel('Programmers')
    plt.title('Most popular languages')
    plt.tight_layout()
    plt.show()
