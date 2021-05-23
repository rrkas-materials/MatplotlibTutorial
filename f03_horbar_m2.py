from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')

    data = pd.read_csv('data/data03.csv')

    ids = data['Responder_id']
    lang_resp = data['LanguagesWorkedWith']

    c = Counter()

    for resp in lang_resp:
        c.update(resp.split(';'))

    # print(c.most_common(15))

    # method 1
    languages = []
    freq = []
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
