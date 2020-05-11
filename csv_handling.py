import csv


with open('text.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_counter = 0
    for row in csv_reader:
        if row_counter ==0:
            print(f'The names of the columns are {",".join(row)}.')
            row_counter += 1
        else:
            print(f'{row[0]} is {row[2]} and {row[1]} years old.')
