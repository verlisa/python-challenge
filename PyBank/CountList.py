# import modules
import csv  
import os
# Open the CSV
with open('budget_data_1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(len(budget_data_1))
