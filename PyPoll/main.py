import os
import csv

csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csv_header = next(csvreader)