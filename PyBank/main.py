import os
import csv

bank_csv = os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join("budget_analysis.txt")
with open(bank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    
    

    total_months=[]
    total_dollars=[]
    profit=[]
    #initial_profit=[]
    pandl=[]
    pandl_list=[]
    total_profit=[]
    greatest_increase_in_profits=["", 9999]
    greatest_decrease_in_profits=["",0]

    initial_profit = 0
    
    for row in csvreader:
        total_months.append(row[0])
        
        total_dollars.append(int(row[1]))
       
        pandl = int(row[1]) - initial_profit
        pandl_list.append(pandl)
        initial_profit=int(row[1])
        length = len(pandl_list)-1

        if pandl > greatest_increase_in_profits[1]:
            greatest_increase_in_profits[0] = row[0]
            greatest_increase_in_profits[1] = pandl

        if pandl < greatest_decrease_in_profits[1]:
            greatest_decrease_in_profits[0] = row[0]
            greatest_decrease_in_profits[1] = pandl  
    month_count = len(total_months)  
    amount = sum(total_dollars)
    total_change = sum(pandl_list[1:])   

    average_change = total_change /length


    
    print(f"Financial Analysis")
    print("--------------------")
    print(f"Total Months:{month_count}")
    print(f"Total:{amount}")
    # print(pandl_list)
    print(f"Average Change:{average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_in_profits[0]} (${greatest_increase_in_profits[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits[0]} (${greatest_decrease_in_profits[1]})")
with open(file_to_output, "w") as txt_file:
    txt_file.write(f'Total Months: $ {month_count}\n' ) 
    txt_file.write(f'Total Sum: $ {amount}\n' )
    txt_file.write(f"Average Change:{average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_in_profits[0]} (${greatest_increase_in_profits[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_in_profits[0]} (${greatest_decrease_in_profits[1]})\n")