import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.style.use('seaborn')

    # x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
    # y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
    #
    # colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
    #
    # sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
    #          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

    data = pd.read_csv('data/data08.csv')
    view_count = data['view_count']
    likes = data['likes']
    ratio = data['ratio']

    # plt.scatter(x, y, s=100, c='green', marker='x')
    # plt.scatter(x, y, s=100, edgecolors='black', linewidths=1, alpha=0.75)
    # plt.scatter(x, y, s=100, c=colors, edgecolors='black', linewidths=1, alpha=0.75)
    # plt.scatter(x, y, s=100, c=colors, cmap='Greens', edgecolors='black', linewidths=1, alpha=0.75)
    # plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolors='black', linewidths=1, alpha=0.75)
    # plt.scatter([2, 5], [5, 6], c='green', s=100, edgecolors='black', linewidths=1, alpha=0.75)
    # cbar = plt.colorbar()
    # cbar.set_label('Satisfaction')

    plt.scatter(
        view_count,
        likes,
        c=ratio,
        cmap='summer',
        edgecolors='black',
        linewidths=1,
        alpha=0.75
    )

    cbar = plt.colorbar()
    cbar.set_label('Like/Dislike Ratio')

    plt.xscale('log')
    plt.yscale('log')

    plt.title('Trending YouTube Videos')
    plt.xlabel('View Count')
    plt.ylabel('Total Likes')

    plt.tight_layout()

    plt.show()
