# python-challenge -- PyPoll

# Import Modules
import os
import csv

# Read csv file
PyPoll_Data = os.path.join("./Unit03 - Python_Homework_PyPoll_Resources_election_data.csv")

with open(PyPoll_Data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    csv_header = next(csvfile)

# Define variables, lists, and dictionaries
    vote_counter = 0
    all_candidates = []
    candidate_vote_totals = {}
    candidate_percent_totals = {}
    percent = float

    # Insert a for loop to count number of rows
    # Number of rows will = total number of votes cast
    for row in csvreader:
        vote_counter += 1

    # Assign a variable to the candidate name
    # Give an index so that when it loops, that location can be stored
        candidate_name = row[2]
        # If the candidate's name has not yet appeared, it will be added to the list
        if candidate_name not in all_candidates:
            all_candidates.append(candidate_name)
            # As candidates are added to this list, they are added
            # to a dictionary that holds {candidate name: candidate votes}
            candidate_vote_totals[candidate_name] = 1

        else: 
            # When a candidate receives another vote, this gets added to their total
            candidate_vote_totals[candidate_name] = candidate_vote_totals[candidate_name] + 1

    # To calculate the percentage of votes:
    # The loop will then capture the value of the individual's vote by
    # their key; then this value is divided by the total amount of votes
    for key, value in candidate_vote_totals.items():
        percent = value / vote_counter

        candidate_percent_totals.update({key: str("{:.3%}".format(percent))})


# Calculate the winner
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# By finding the key that corresponds with highest vote value total
max(candidate_vote_totals, key=lambda key: candidate_vote_totals[key]) 

# Print out the results
print("Election Results")
print("------------------------")
print("Total Votes: " + str(vote_counter))
print("The number of votes each candidate received was: " + str(candidate_vote_totals))
print("The percentage of votes each candidate received was: " + str(candidate_percent_totals)) 
print("Winner: " + str(max(candidate_vote_totals, key=lambda key: candidate_vote_totals[key])))

# Export the results to a text file
# Export the results to a text file
f= open("Election_Results.txt", "w+")
f.write("Election Results --- Total Votes: " + str(vote_counter) + " The number of votes each candidate received was: " + str(candidate_vote_totals) + " The percentage of votes each candidate received was: " + str(candidate_percent_totals) + " The Winner: " + str(max(candidate_vote_totals, key=lambda key: candidate_vote_totals[key])))
f.close()