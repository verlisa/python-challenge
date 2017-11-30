# import modules
import csv  
import os
# Lists to store data
Date =[]
Revenue = []
# Open the CSV
with open('budget_data_1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        # Add date from each row
    for value in csvreader:
        print(value)
    