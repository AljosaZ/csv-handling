import csv


with open('text.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for count, row in enumerate(csv_reader):
        if count > 0:
            print(f'{row[0]} is {row[2]} and {row[1]} years old.')
