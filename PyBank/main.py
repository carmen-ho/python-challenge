import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    # csv_header = next(csvreader)
    # # print(f"CSV Header: {csv_header}")

    # date = list(csvreader)

    # monthcount = len(date)
    # print("Total Months: " + str(monthcount))

  
    # total = 0
    # for row in csv.reader(csvfile):
    #     # total = int(row[1])
    #     total = sum(int(r[1]) for r in csv.reader(csvfile))
    # print ("Total: $" + str(total))

    # budget_df
    # budget_df['Change'].mean()












    










