# Import Modules
import os
import csv
import datetime

# Set path for file
# datapath = os.path.join("Resources", "budget_data.csv")
# for VS Code debugging use this path
datapath = 'C:/Users/JBStogner/GitHub/python-challenge/PyBank/Resources/budget_data.csv'

# Declare Variables
# Is there a better way to do this? Without this formatting the date defaults to an int.
MinDate = datetime.datetime.strptime('2099, 1, 1', '%Y, %m, %d').date()
MaxDate = datetime.datetime.strptime('1899, 1, 1', '%Y, %m, %d').date()

# print(was_date1_before)
# Open the data
with open(datapath) as datafile:
    # Read the file using the csv module
    datareader = csv.reader(datafile, delimiter=",")
    # Skip the header row
    next(datareader)
    for row in datareader:
        # Find the start date and the end date
        Date = (datetime.datetime.strptime(row[0], '%b-%y').date())
        if Date < MinDate:
            MinDate = Date
        if Date > MaxDate:
            MaxDate = Date

# Formula from https://kite.com/python/answers/how-to-get-the-number-of-months-between-two-dates-in-python
num_months = (MaxDate.year - MinDate.year) * 12 + (MaxDate.month - MinDate.month)
print(num_months)
print(MaxDate)
print(MinDate)

#         # Find net total Profit/Loss over the entire period


# # date_str = 'Dec-17' # The date - 29 Dec 2017
# # format_str = '%b-%y' # The format
# # datetime_obj = datetime.datetime.strptime(date_str, format_str)
# # print(datetime_obj.date())



# # Average of all changes in "Profit/Losses" across the entire period

# # Find the greatest increase in profits (date and amount) across the entire period

# # Find the greatest decrease in lossess (date and amount) across the entire period

# # Example Output

# #   ```text
# #   Financial Analysis
# #   ----------------------------
# #   Total Months: 86
# #   Total: $38382578
# #   Average  Change: $-2315.12
# #   Greatest Increase in Profits: Feb-2012 ($1926159)
# #   Greatest Decrease in Profits: Sep-2013 ($-2196167)
# #   ```

# # The Output should print to the terminal and export a text file with the results