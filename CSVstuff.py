import csv

def write_list(_list, filename='new'):
    with open(filename + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in _list:
            writer.writerow(row)
