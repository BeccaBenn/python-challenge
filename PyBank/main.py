#Reading the resource file
import os
import csv
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

#Variables 
month_count = 0
profit_loss_tot = 0
total_change = 0
profit_loss_list = []
greatest_increase = 0
greatest_decrease = 0
date_list = []
with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)

   #itterate through CSV file
   for row in csvreader:
       #Count the number of months by finding length of file (one month per row)
       month_count += 1

       #Total the net "Profit/Losses"
       profit_loss = int(row[1])
       profit_loss_tot += profit_loss

       #Create list to store values
       profit_loss_list.append(profit_loss)

       #store the indexes of the dates

    #    dates = (row,[0])
    #    date_list.append(dates)
    #    print(date_list)

       
    #    row_index = row
    #    date_column_index = 0

   #find total change within list, then find average of the change and format    
   for i in range(1, len(profit_loss_list)):
    change = profit_loss_list[i] - profit_loss_list[i - 1]
    total_change += change 
    avg_change = total_change/month_count
    avg_change_f = f"{avg_change:.2f}"
    
    
    #Find the greastest increase and decrease in profits
    if change > greatest_increase:
       greatest_increase = change
    #    row = i
    #    increase_date = csvreader[row][0]
       
    elif change < greatest_decrease:
        greatest_decrease = change 
        # row = i
        # decrease_date = csvreader[row][0]
     
    
             
       #right here i is the row count that has the date 
       #but it's in the profitloss list, which doesn't have the dates
#     # for current_row_index, row in enumerate(csvreader):
#         # if current_row_index == row_index:
#             try:
#                 date = row[date_column_index]
#                 break  # Exit the loop once the value is found
#             except IndexError:
#                 continue

# # Check if the specific value was found
# if date is not None:
#     print(date)
# else:
    
    
   
   print(f"Total Months: {month_count} ")
   print(f"Total: ${profit_loss_tot}")
   print(f"The total change in profits and losses for the entire period are ${total_change}.")
   print(f"Average Change: ${avg_change_f}")
   print(f"Greatest Increase in Profits: ${greatest_increase}")
   print(f"Greatest Decrease in Profits: ${greatest_decrease}")
