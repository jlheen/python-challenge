# python-challenge -- PyBank

# Import Modules
import os
import csv
import statistics

# Create lists to store data from CSV
date = []
profit_losses = []
profit_changes = []
date_and_profits = {}

# Assign variables
total_months = float
net_total = float

# Reading the CSV File
#--------------------------------------

pyBank_csv = os.path.join("./PyBank_BudgetData.csv")

with open(pyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    for row in csvreader:
        # Add Dates
        date.append(row[0])
        # Add Profit/Losses
        profit_losses.append(row[1])
        

# Calculating the Financial Analysis Values
#-------------------------------------
# In order to calculate the total count of months
# changing the Profits/Losses list from strings to floats
profit_losses=list(map(float, profit_losses))

# Find the length of this list, which equates to the amount of PyBank entries
len(profit_losses)
# Assign this value to the total_months variable
total_months = len(profit_losses)

# Calculate the Net Total Amount of Profits/Losses over the entire period
sum(profit_losses)
# Assign this to the net_total variable
net_total = sum(profit_losses)

# Calculate the changes between profits and losses each month and assign the variable
# https://stackoverflow.com/questions/39088546/python-subtracting-elements-in-a-lists-from-previous-element
profit_changes = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses) -1)]

# Calculate the average change over this list of profit changes
from statistics import mean
mean(profit_changes)

# Create a dictionary to hold the dates and amounts of the changes in profit
# In order to do so, need to add a zero to correspond with first month in the profit_changes list
# https://www.geeksforgeeks.org/python-list-insert/
profit_changes.insert(0, 0)

# source: https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
# using zip() 
# to convert lists to dictionary 
date_and_profits = dict(zip(date, profit_changes))

# Calculate the max value of the profit changes
# https://stackoverflow.com/questions/26871866/print-highest-value-in-dict-with-key
# This corresponds to the greatest increase
max(date_and_profits.items(), key=lambda k: k[1])


# Calculate the min value of the profit changes
min(date_and_profits.items(), key=lambda k: k[1])


#Print the Financial Analysis
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total)) 
print("Average Change: $" + str(mean(profit_changes)))
print("Greatest Increase in Profits: " + str(max(date_and_profits.items(), key=lambda k: k[1])))
print("Greatest Decrease in Profits: " + str(min(date_and_profits.items(), key=lambda k: k[1])))

# Export the results to a text file
f= open("Financial_Analysis.txt", "w+")
f.write("Financial Analysis --- Total Months: " + str(total_months) + " Total: $" + str(net_total) + " Average Change: " + str(mean(profit_changes)) + "Greatest Increase in Profits: " + str(max(date_and_profits.items(), key=lambda k: k[1])) + "Greatest Decrease in Profits: " + str(min(date_and_profits.items(), key=lambda k: k[1])))
f.close()