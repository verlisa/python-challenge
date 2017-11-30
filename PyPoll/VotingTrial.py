# import modules
import csv
import os
# Lists to store data
voterID =[]
county = []
candidate = []
# Open the CSV and read it
csvpath = os.path.join ('..', 'PyPoll', 'election_data_1.csv')
with open('election_data_1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header
    next(csvreader, None)        
        # Add date from each row
    for row in csvreader:
      # Add voter ID
        voterID.append(row[0])
    print("Total Votes: " + str(len(voterID)))
      # Add candidate name
    candidate.append(row[2])
# Check for unique values
UniqCand = []
for i in candidate:
    if i not in UniqCand:
        UniqCand.append(i)
print (UniqCand)

