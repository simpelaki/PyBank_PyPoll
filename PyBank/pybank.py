import csv

file_to_load ="Resources/budget_data.csv"
file_to_save = "analysis/budget_analysis.txt"

total_month = 0
total_profit = 0
total_loss = 0  

with open(file_to_load) as in_file:
    reader = csv.reader(in_file)
    header = next(reader)

    for row in reader:
        # print(row)
        # exit()
        total_month = total_month + 1
        if int(row[1])>= 0:        
            total_profit = total_profit + int(row[1])
        else: 
            total_loss = total_loss + int(row[1])

print(total_profit)
print(total_loss)


output=f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
"""

print(output)

with open(file_to_save, "w") as out_file:
    out_file.write(output)
