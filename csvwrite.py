#!usr/bin/python3

import csv, tws

def write_table_to_csv(table):
    rows = tws.get_rows(table)
    with open('weapons.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for row in rows:
            row_data = tws.get_row_data(row)
            print(row_data)
            writer.writerow(row_data)

def write_rows_to_csv(rows, filename):
    with open('CSVs/' + filename + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for row in rows:
            writer.writerow(row)
