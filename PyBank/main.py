import os
import csv

# Defining the path/location of the CSV file.
csvpath = 'Resources/budget_data.csv'

# Opening the CSV file, reading the file, defining the delimiter,
# and skipping the header.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Listing the variables and defining where specific data is found.  
    total_months =0
    total_months += 1
    total_profit_loss = 0
    first_line = next(csvreader)
    total_profit_loss += int(first_line[1])
    pre = int(first_line[1])
    great_inc = ['',0]
    great_dec = ['',0]
    change_list = []
    
# Starting a for loop to read the CSV file lines, capture the total months 
    # and total profits/losses. 
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        number = int(row[1]) - pre
        pre = int(row[1])
        change_list.append(number)

# Creating 2 If statements to capture the greatest increase and gretest decrease 
        # and the month that the increase or decrease happened.
        if number > great_inc[1]:
            great_inc[1] = number
            great_inc[0] = row[0]
        if number < great_dec[1]:
            great_dec[1] = number
            great_dec[0] = row[0]

# Calculating the average chage in profits/losses for the entire data set.
ave_change = float(sum(change_list))/ len(change_list)

# Defining the results of the above code to be used as the information for the text file.
result = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${ave_change:.2f}
Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})
Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})
"""

# Printing the results, creating the file that the results will be staved in. Opening the 
# text file just created and writing the results into the file.
print(result)
output = 'analysis/budget_analysis.txt'
with open (output, 'w') as file:
    file.write (result)