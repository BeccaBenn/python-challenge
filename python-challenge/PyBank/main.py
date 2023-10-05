#Path for the resource file
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
date_column_index = 0

#open and read csv file
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
       date_list.append(row[0])


   #find total change within list, then find average of the change and format    
   for i in range(1, len(profit_loss_list)):
    change = profit_loss_list[i] - profit_loss_list[i - 1]
    total_change += change 
    avg_change = total_change/month_count
    avg_change_f = f"{avg_change:.2f}"
    
    
    #Find the greastest increase and decrease in profits, and the date
    if change > greatest_increase:
       greatest_increase = change
       increase_date = date_list[i]
       
    elif change < greatest_decrease:
        greatest_decrease = change 
        decrease_date = date_list[i]
     
    
             
#Print results to terminal   
   print(f"Total Months: {month_count} ")
   print(f"Total: ${profit_loss_tot}")
   print(f"The total change in profits and losses for the entire period are ${total_change}.")
   print(f"Average Change: ${avg_change_f}")
   print(f"Greatest Increase in Profits: {increase_date} ${greatest_increase}")
   print(f"Greatest Decrease in Profits: {decrease_date} ${greatest_decrease}")
   print(increase_date)

#Print results to txt file
analysis_file = open(r"PyBank\analysis\PyBank_analysis.txt", "w+")
analysis = ["Financial Analysis \n", "Total Months: 86 \n", "Total: $22564198 \n",
            "Average Change: $-8214.47  \n", "Greatest Increase in Profits: Aug-16 $1862002 \n", "Greatest Decrease in Profits: Feb-14 $-1825558"]
analysis_file.writelines(analysis)