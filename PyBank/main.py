import os
import csv

csvpath = 'Resources/budget_data.csv'

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
        
    total_months =0
    total_months += 1
    total_profit_loss = 0
    
    first_line = next(csvreader)
    total_profit_loss += int(first_line[1])
    pre = int(first_line[1])
    great_inc = ['',0]
    great_dec = ['',0]
    change_list = []
<<<<<<< HEAD
    
=======
>>>>>>> 6d97ba45c70638ff1cd1e34c4189ce05a5a6455b
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        number = int(row[1]) - pre
        pre = int(row[1])
        change_list.append(number)
        if number > great_inc[1]:
            great_inc[1] = number
            great_inc[0] = row[0]
        if number < great_dec[1]:
            great_dec[1] = number
            great_dec[0] = row[0]

ave_change = float(sum(change_list))/ len(change_list)

result = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${ave_change:.2f}
Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})
Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})
"""
print(result)
output = 'analysis/budget_analysis.txt'
with open (output, 'w') as file:
    file.write (result)