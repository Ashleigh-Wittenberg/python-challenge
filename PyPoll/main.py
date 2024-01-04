import os
import csv


#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = 'Resources/election_data.csv'

#def print_percentages(election_data):

candidate_list = []
total_vote = 0


# need to count the # of times the candidates name appears 
# print the candidtaes name with the percentge of votes they recieved 
# and the total they recieved
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for line in csvfile:
        total_vote += 1
        candidate = (line[3])
        if candidate not in candidate_list:
            candidate_list.append (candidate)
print('Election Results')

total_votes = sum(1 for row in csvreader)
print(f'Total Votes: {total_votes}')