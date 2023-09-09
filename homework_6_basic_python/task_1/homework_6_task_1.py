import csv

with open('test_file.csv', 'r', newline='') as file:
    data = list(csv.reader(file))

for line in range(1, len(data)):
    for value in range(1, len(data[line])):
        try:
            data[line][value] = str(float(data[line][value]) * 36.5)
        except ValueError:
            pass

with open('salaries_uah.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
