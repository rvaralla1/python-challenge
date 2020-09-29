import os
import csv

bank_csv = 'Resources/budget_data.csv'

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:  

        date = str(bank_csv[0])
        pandl = str(bank_csv[1])

        count = 0
        total = 0
        total_months = len(bank_csv[0])
        total_pandl = float(sum(pandl))
        average_change = total_pandl / total_months
        greatest_increase_in_profits = []
        greatest_decrease_in_profits = []

        print(f"Financial Analysis")
        print("--------------------")
        print(f"Total Months:{total_months}")
        print(f"Total:{total_pandl}")
        print(f"Average Change:{average_change}")
        print(f"Greatest Increase in Profits:{greatest_increase_in_profits}")
        print(f"Greatest Decrease in Profits:{greatest_decrease_in_profits}")

touch(bank_data)
    print(f"Financial Analysis")
    print("--------------------")
    print(f"Total Months:{total_months}")
    print(f"Total:{total_pandl}")
    print(f"Average Change:{average_change}")
    print(f"Greatest Increase in Profits:{greatest_increase_in_profits}")
    print(f"Greatest Decrease in Profits:{greatest_decrease_in_profits}")