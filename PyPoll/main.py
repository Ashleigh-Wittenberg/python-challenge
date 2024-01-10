import os
import csv

csvpath = 'Resources/election_data.csv'

candidate_list = []
total_vote = 0
indiv_vote = {}
max_votes = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for line in csvreader:
        total_vote += 1
        candidate = (line[2])

        if candidate not in candidate_list:
            candidate_list.append (candidate)
            indiv_vote[candidate]= 0

        indiv_vote[candidate] += 1

    for candidate, votes in indiv_vote.items():
        percentage = (votes / total_vote) * 100
        if votes > max_votes:
            max_votes = votes
            winner = candidate
        print(f'{candidate}: {percentage:.3f}% ({votes})')
  

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

print(result)
output = 'analysis/election_analysis.txt'
with open (output, 'w') as file:
    file.write (result)