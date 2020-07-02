# Import Modules
import os
import csv
import datetime

# Set path for file
datapath = os.path.join("Resources", "budget_data.csv")
# Set output path for file
output_path = os.path.join("analysis", "analysis.txt")
# for VS Code debugging use this file path
# datapath = 'C:/Users/JBStogner/GitHub/python-challenge/PyBank/Resources/budget_data.csv'

# Declare Variables
MinDate = datetime.datetime.strptime('2099, 1, 1', '%Y, %m, %d').date()
MaxDate = datetime.datetime.strptime('1899, 1, 1', '%Y, %m, %d').date()
MaxProfit = 0
MinProfit = 0
NetIncome = 0
net_change = 0
prev_value = 0
months_of_data = 0
sum_change = 0
net_change_list = []

# Open the data
with open(datapath) as datafile:
    # Read the file using the csv module
    datareader = csv.reader(datafile, delimiter=",")
    # Skip the header row
    next(datareader)
    for row in datareader:
        # Count the periods for which there are data
        months_of_data = months_of_data + 1
        # Find the start date and the end date
        Date = datetime.datetime.strptime(row[0], '%b-%Y').date()
        if Date < MinDate:
            MinDate = Date
        elif Date > MaxDate:
            MaxDate = Date
        # Find net total Profit/Loss over the entire period
        NetIncome = NetIncome + int(row[1])
        # Find the max/min changes to profits and the corresponding dates
        net_change = int(row[1]) - prev_value
        prev_value = int(row[1])
        if net_change < MinProfit:
                MinProfit = net_change
                MinProfitDate = row[0]
        elif net_change > MaxProfit:
                MaxProfit = net_change
                MaxProfitDate = row[0]
        # Track net_change in a list to determine average profit change
        net_change_list.append(net_change)
    
# Get the number of months between the start and stop dates
# Formula from https://kite.com/python/answers/how-to-get-the-number-of-months-between-two-dates-in-python
num_months = (MaxDate.year - MinDate.year) * 12 + (MaxDate.month - MinDate.month)
# Get the average monthly change & skip the first row in the list because it is not a measure of change
profit_change_iterator = iter(net_change_list)
next(profit_change_iterator)
for profit_change in profit_change_iterator:
    sum_change = sum_change + profit_change
average_change = sum_change / num_months

print("Financial Analysis")
print("----------------------------")
# Print the number of months between start and stop dates
print(f'Total Months: {months_of_data}')
# Print the Net Income for the period
print(f'Total ${NetIncome}')
# Print the average monthly change
formatAvgChange = ("%.2f" % average_change)
print(f'Average Change: ${formatAvgChange}')
# Print Max Profit
print(f'Greatest Increase in Profits: {MaxProfitDate} (${MaxProfit})')
# Print Min Profit
print(f'Greatest Decrease in Profits: {MinProfitDate} (${MinProfit})')

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w')

file.write('Financial Analysis')
file.write('\n''----------------------------')
file.write('\n'f'Total Months: {months_of_data}')
file.write('\n'f'Total ${NetIncome}')
file.write('\n'f'Average Change: ${formatAvgChange}')
file.write('\n'f'Greatest Increase in Profits: {MaxProfitDate} (${MaxProfit})')
file.write('\n'f'Greatest Decrease in Profits: {MinProfitDate} (${MinProfit})')