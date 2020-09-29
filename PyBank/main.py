import os
import csv

bank_csv = 'Resources/budget_data.csv'


print(f"Financial Analysis")


Total Months = []
Total = []
Average Change = []
Greatest Increase in Profits = []
Greatest Decrease in Profits = []

Total Months = int(len(bank_csv[0])

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        

    print(csvreader)

    csv_header = next(csvreader)
    


for row in csvreader:
        print(row)