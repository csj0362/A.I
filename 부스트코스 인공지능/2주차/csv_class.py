import csv
import pprint
file_path = "./data-01-test-score.csv"

class ReadCSV():
  
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_list=[]

    def read_file(self):
        f = open(self.file_path, 'r', encoding = 'utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.file_list.append(line)
        f.close()
        return self.file_list

    def merge_list(self):
        int_list, sum_list = [], []
        for i in range(len(self.file_list)):
            int_list.append(list(map(int, self.file_list[i])))
            sum_list.append(sum(int_list[i])) 
        return sum_list

read_csv = ReadCSV(file_path)
pprint.pprint(read_csv.read_file())
print(read_csv.merge_list())
