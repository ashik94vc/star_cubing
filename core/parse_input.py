import csv

def parseInput(filename):
    csvfile = open(filename, newline='')

    list_map = list()
    input_table = list()

    csvreader = csv.reader(csvfile)

    missing_char = '?'

    for row in csvreader:
        if missing_char in row:
            continue
        input_table.append(row)
        for column_index in range(len(row)):
            if len(list_map) == len(row):
                if row[column_index] in list_map[column_index]:
                    list_map[column_index][row[column_index]] += 1
                else:
                    list_map[column_index][row[column_index]] = 1
            else:
                list_map.append({row[column_index]: 1})

    return list_map,input_table
