import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)    # to handle the header

    row = 0
    profit = 0
    loss = 0
    net_total = 0
    row_of_profit = 0
    row_of_loss = 0
    # min = 0
    # max = 0

    average_pl = 0
    total_pl = 0
    changes_pl = []
    # current_pl = 0
    # end_pl = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999]

    month_count = 0
    month_total = 0
    
    month_total += 1
    first_row = next(csvreader)    # to handle the first month
    total_pl += int(first_row[1])
    prev_net = int(first_row[1])   # set the value of first month as previous net
    

    for row in csvreader:
        
        month_total += 1
        total_pl += int(row[1])
        
        net_total = net_total + int(row[1])
        net_change = int(row[1]) - prev_net  # value of current month - value of previous month
        prev_net = int(row[1])               # update value of previous month

        changes_pl += [net_change]

       
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        

    average_pl = sum(changes_pl) / len(changes_pl)

            
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {month_total} ")
print(f"Total: ${total_pl}")
print(f"Average Change: ${average_pl:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


data_output = os.path.join("Analysis", "bankdata.csv")

with open(data_output, 'w') as csvfile:
    csvfile.write(f"Financial Analysis\n")
    csvfile.write(f"------------------------\n")
    csvfile.write(f"Total Months:{month_total}\n ")
    csvfile.write(f"Total: ${total_pl}\n")
    csvfile.write(f"Average Change: ${average_pl:.2f}\n")
    csvfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    csvfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

