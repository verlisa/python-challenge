# import modules
import csv  
import os

# Lists to store data
date =[]
revenue = []
revdiff = []
# Open the CSV file and read the data
with open('budget_data_1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    next(csvreader, None)        
        # Append date from each row
    for row in csvreader:
      #Add revenue
        revenue.append(row[1])
# Create two lists with the revenue values using zip 
    NewRev=[int(j)-int(i) for i, j in zip(revenue[:-1], revenue[1:])]
    revdiff = (list(NewRev))
    NewTotal = sum(int(p) for p in revdiff)
    print("Total Revenue: " + "$" + str(NewTotal))
# Maximum difference and index
max_value = max(revdiff)
print("Greatest Increase in Revenue " + str(max_value))
# Zip the column from date with difference column for revenue
IdxRef = zip(date, revdiff)
# NEED TO COMPLETE INDEX
# Minimum difference and index
min_value = min(revdiff)
print("Greatest Decrease in Revenue " + str(min_value))
print(NewRev)