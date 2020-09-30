import os
import csv

bank_csv = os.path.join('Resources', 'budget_data.csv')

with open(bank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    first_row = next(csvreader)
    x = first_row[1]
    

    total_months=[]
    total_dollars=[]
    profit=[]
    initial_profit=[]
    pandl=[]
    pandl_list=[]
    total_profit=[]
    greatest_increase_in_profits=[]
    greatest_decrease_in_profits=[]

    initial_profit = x

    for row in csvreader:
        total_months.append(row[0])
        total_dollars.append(int(row[1]))

        initial_profit = int(profit[x])

        pandl = (initial_profit - int(profit[x-1]))
        pandl_list.append(pandl)

        total_profit = sum(pandl_list)

        average_change = total_dollars / len(total_months)

        greatest_increase_in_profits = max([1])
        greatest_increase_month = pandl.index(greatest_increase_in_profits)

        greatest_decrease_in_profits = min([1])
        greatest_decrease_month = pandl.index(greatest_decrease_in_profits)

        print(f"Financial Analysis")
        print("--------------------")
        print(f"Total Months:{len(total_months)}")
        print(f"Total:{sum(total_dollars)}")
        print(f"Average Change:{average_change}")
        print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profits})")
        print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_in_profits})")

f= open("financial.txt","w+")
for i in range(7):
    f.write(

        (f"Financial Analysis")
        (f"Total Months:{len(total_months)}")
        (f"Total:{sum(total_dollars)}")
        (f"Average Change:{average_change}")
        (f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profits})")
        (f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_in_profits})")
    )
    f.close()