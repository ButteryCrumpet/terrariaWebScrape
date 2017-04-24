import csv

def write_list(_list, filename='new'):
    with open(filename + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in _list:
            writer.writerow(row)

def read_rows(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append(row)
    return rows

def write_dict(_dict, fieldnames ,filename='new'):
    with open(filename+'.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in _dict:
            writer.writerow(item)

def read_to_dict(filename):
    dicts = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dicts.append(row)
    return dicts
