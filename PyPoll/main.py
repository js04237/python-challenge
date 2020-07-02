# Import Modules
import os
import csv

# Set path for file
datapath = os.path.join("Resources", "election_data.csv")
# Set output path for file
output_path = os.path.join("analysis", "analysis.txt")
# for VS Code debugging use this file path
# datapath = 'C:/Users/JBStogner/GitHub/python-challenge/PyPoll/Resources/election_data.csv'

# Declare Variables
votes = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0
candidate_list = []
# Open the data
with open(datapath) as datafile:
    # Read the file using the csv module
    datareader = csv.reader(datafile, delimiter=",")
    # Skip the header row
    next(datareader)
    for row in datareader:
        # Count the periods for which there are data
        votes = votes + 1
        # Find the names of the candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2] == 'Khan':
            khan_count = khan_count + 1
        elif row[2] == 'Correy':
            correy_count = correy_count + 1
        elif row[2] == 'Li':
            li_count = li_count + 1
        elif row[2] == "O'Tooley":
            otooley_count = otooley_count + 1

# Identify the winner of the election
vote_list = (khan_count, correy_count, li_count, otooley_count)
maxlist = max(vote_list)
if otooley_count == maxlist:
    winner = "O'Tooley"
elif li_count == maxlist:
    winner = 'Li'
elif correy_count == maxlist:
    winner = 'Correy'
elif khan_count == maxlist:
    winner = 'Khan'

# Calculate vote percentages for each candidate
khan_percent = '%.3f' % ((khan_count / votes) * 100)
correy_percent = '%.3f' % ((correy_count / votes) * 100)
li_percent = '%.3f' % ((li_count / votes) * 100)
otooley_percent = '%.3f' % ((otooley_count / votes) * 100)

print('Election Results')
print('-------------------------')
# Print the number of votes
print(f'Total Votes: {votes}')
print('-------------------------')
# Print Vote percentages
print(f'Khan: {khan_percent}% ({khan_count})')
print(f'Correy: {correy_percent}% ({correy_count})')
print(f'Li: {li_percent}% ({li_count})')
print(f"O'Tooley: {otooley_percent}% ({otooley_count})")
print('-------------------------')
# Print the winner
print(f'Winner: {winner}')
print('-------------------------')

# Open the file using "write" mode. '\n' makes each write happen on a new line
file = open(output_path, 'w')

file.write('Election Results')
file.write('\n''-------------------------')
file.write('\n'f'Total Votes: {votes}')
file.write('\n''-------------------------')
file.write('\n'f'Khan: {khan_percent}% ({khan_count})')
file.write('\n'f'Correy: {correy_percent}% ({correy_count})')
file.write('\n'f'Li: {li_percent}% ({li_count})')
file.write('\n'f"O'Tooley: {otooley_percent}% ({otooley_count})")
file.write('\n'f'-------------------------')
file.write('\n'f'Winner: {winner}')
file.write('\n'f'-------------------------')