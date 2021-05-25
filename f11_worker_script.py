import csv
import random
import time

if __name__ == '__main__':
    x_value = 0
    total_1 = 1000
    total_2 = 1000

    fieldnames = ["x_value", "total_1", "total_2"]

    with open('data/data11.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while True:
        with open('data/data11.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2
            }

            csv_writer.writerow(info)
            print(x_value, total_1, total_2)

            x_value += 1
            total_1 = total_1 + random.randint(-20, 30)
            total_2 = total_2 + random.randint(-10, 15)

        time.sleep(1)