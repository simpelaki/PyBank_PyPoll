import csv

file_to_load = "Resources/election_data.csv"
file_to_save = "election_data.txt"

total_votes = 0 

# Open and read csv
with open(file_to_load) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")
    candidates = {}
    percentage = {}

    # Read through each row of data after the header
    for row in csv_reader:
        total_votes = total_votes +1    

    # Ballot ID,County,Candidate
        current_candidate=row[2]
        if current_candidate in candidates:
            candidates[current_candidate] = candidates[current_candidate] +1
        else:  
            candidates[current_candidate]=1
print(f"My_Total_Votes: {total_votes}")
print(f"candidates_and_vote: {candidates}")

for key in candidates:
    if key not in percentage:
        percentage[key]= candidates[key] / total_votes
print(f"candidates_and_percentage: {percentage}")

winner = ""
winner_vote = 0

for key in candidates:
    if candidates[key] >= winner_vote:
        winner = key
        winner_vote = candidates[key]

print(f"winner: {winner}")
print(f"winner_vote: {winner_vote}")


output=f"""
Election Results
----------------------------
Total Votes: {total_votes}
-------------------------
candidates_and_vote: {candidates}
candidates_and_percentage: {percentage}
-------------------------
winner: {winner}

"""

print(output)

with open(file_to_save, "w") as out_file:
    out_file.write(output)


        # # Print a the summary of the analysis
        # Charles_percent = (Charles_Casper/total_votes) *100
        # Diana_percent = (Diana_DeGette/total_votes) * 100
        # Raymon_percent = (Raymon_Anthony_Doane/total_votes)* 100


 


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# ------------------------- 
