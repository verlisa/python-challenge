# import modules
import csv  
import os
# Lists to store data
date =[]
revenue = []
# Open the CSV
with open('budget_data_1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header
    next(csvreader, None)        
        # Add date from each row
    for row in csvreader:
      # Add date rows to one list using the index and excluding header using append
        date.append(row[0])
        revenue.append(row[1])
        
    print(len(date))

# Print total months
print("Total Months: " + str(len(date)))
Total = sum(int(i) for i in revenue)
print("Total Revenue: " + "$" + str(Total))