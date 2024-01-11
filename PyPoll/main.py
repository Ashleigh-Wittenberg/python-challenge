import os
import csv

# Defining the path/location of the CSV file.
csvpath = 'Resources/election_data.csv'

# Listing the variables
candidate_list = []
total_vote = 0
indiv_vote = {}
max_votes = 0

# Opening the CSV file, reading the file, defining the delimiter,
    # and skipping the header.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Starting a for loop to read the CSV file lines, capture the total votes added 1 by 1,
    # and calling out where the candidate variable is in the data. 
    for line in csvreader:
        total_vote += 1
        candidate = (line[2])

# Creating an If statment to add the candidate names to a list and setting the 
        # individual vote to 0.
        if candidate not in candidate_list:
            candidate_list.append (candidate)
            indiv_vote[candidate]= 0

# Adding up all the votes for each candidate 
        indiv_vote[candidate] += 1

# Starting another for loop to calculate the percentage of the votes each candidate recieved
        # as well as determining the winner of the popular vote based on who recieved the 
        # most votes.
    for candidate, votes in indiv_vote.items():
        percentage = (votes / total_vote) * 100
        if votes > max_votes:
            max_votes = votes
            winner = candidate
        print(f'{candidate}: {percentage:.3f}% ({votes})')
  
# Defining the results of the above code to be used as the information for the text file.
result = f"""
Election Results
-------------------------
Total Votes: {total_vote}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: {winner}
-------------------------
"""

# Printing the results, creating the file that the results will be staved in. Opening the 
# text file just created and writing the results into the file.
print(result)
output = 'analysis/election_analysis.txt'
with open (output, 'w') as file:
    file.write (result)
