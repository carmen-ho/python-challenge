import os
import csv

csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

# A complete list of candidates who received votes

    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

# loop thru to count votes

    for row in csvreader: 

        total_votes +=1

        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

# create a dictionary to put candidates and vote together then use key to find max out of list

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

candidates_and_votes = dict(zip(candidates,votes))
key = max(candidates_and_votes, key=candidates_and_votes.get)

# calculate % of votes

khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#to print statement


print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"-----------------------")
print(f"Winner: {key}")
print(f"-----------------------")

#to write to csv file


data_output = os.path.join("Analysis", "bankdata.csv")

with open(data_output,"w") as csvfile:

    csvfile.write(f"Election Results\n")
    csvfile.write(f"------------------------\n")
    csvfile.write(f"Total Votes: {total_votes}\n")
    csvfile.write(f"------------------------\n")
    csvfile.write(f"Khan: {khan_percent:.3f}% ({khan_votes})\n")
    csvfile.write(f"Correy: {correy_percent:.3f}% ({correy_votes})\n")
    csvfile.write(f"Li: {li_percent:.3f}% ({li_votes})\n")
    csvfile.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n")
    csvfile.write(f"-----------------------\n")
    csvfile.write(f"Winner: {key}\n")
    csvfile.write(f"-----------------------")



