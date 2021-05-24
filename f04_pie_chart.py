from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')

    slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
    labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++',
              'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
    # colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
    explode = [0, 0, 0, 0.2, 0]

    plt.pie(
        slices[:5],
        labels=labels[:5],
        shadow=True,
        startangle=90,
        explode=explode,
        wedgeprops={'edgecolor': 'black'},
        autopct='%1.1f%%'
    )

    plt.title("Pie Chart")
    plt.tight_layout()
    plt.show()
