# import modules
import csv  
import os

# Lists to store data
date =[]
revenue = []
# Open the CSV file and read the data
with open('budget_data_1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    next(csvreader, None)        
        # Append date from each row
    for row in csvreader:
      #Add revenue
        revenue.append(row[1])
        NewRevList=revenue.append(row[1])
difference = []
for i in range(len(NewRevList)-1):
    diffs = abs(NewRevList[i] - NewRevList[i+1])
    difference.append(diffs)
print(difference)