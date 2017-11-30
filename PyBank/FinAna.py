import csv
import os
csvpath = os.path.join('Resources', 'budget_data_1.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    