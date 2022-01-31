import csv
import pprint

file_path = "./data-01-test-score.csv"

def read_file(file_path):
    f = open(file_path, 'r', encoding = 'utf-8')
    file_list = []
    rdr = csv.reader(f)
    for line in rdr:
        file_list.append(line)
    pprint.pprint(file_list)
    f.close()

read_file(file_path)