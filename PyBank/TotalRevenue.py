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
        # Add date from each row
    for row in csvreader:
      #Add revenue
        revenue.append(row[1])
    print(revenue)
Total = sum(int(i) for i in revenue)
print("Total Revenue: " + "$" + str(Total))