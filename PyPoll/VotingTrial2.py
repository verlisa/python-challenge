# import modules
import csv  
import os
# Lists to store data
voterID =[]
county = []
candidate = []
# Open the CSV
csvpath = os.path.join ('..', 'PyPoll', 'election_data_1.csv')
with open('election_data_1.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header
    next(csvreader, None)        
        # Add date from each row
    for row in csvreader:
      # Add voter ID
        voterID.append(row[0])
        candidate.append(row[2])
    unique_candidates = set(candidate)
    print(unique_candidates)
    # print(len(voterID))
    print("Total Votes: " + str(len(voterID)))
