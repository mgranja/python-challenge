import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

months = []
revenue = []
revenue_change = []

previous_revenue = 0

with open(budget_data, newline="", encoding = "utf-8" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csv_header = next(csvreader)
       # print(f"CSV Header: {csv_header}")

    for row in csvreader:

       months.append(row[0])
       revenue.append(int(row[1]))

    # find revenue change

    for x in range(1, len(revenue)):
        revenue_difference = int(revenue[x]) - int(revenue[x-1])
        revenue_change.append(revenue_difference)        
        
# calculate total length of months 
total_months = len(months)

# calculate total revenue
total_revenue = sum(revenue)
      
# calculate average revenue change
revenue_change_average = sum(revenue_change) / len(revenue_change)

# greatest increase in revenue
greatest_increase = max(revenue_change)
# greatest decrease in revenue
greatest_decrease = min(revenue_change)


#Print Results
print("Financial Analysis")
print("......................................................")
print(f"Total Months: {total_months}")
print(f"Total: {total_revenue}")
print(f"Average change:{revenue_change_average}")
print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " ($" + str(greatest_decrease) + ")")

#Output File

Output_file = open("bank_results.txt","w")
            
Output_file.write("Financial Analysis \n")
Output_file.write("---------------------------------------------- \n")
Output_file.write(f"Total Month: {total_months} \n")
Output_file.write(f"Total: {total_revenue} \n")
Output_file.write(f"Average Change: {revenue_change_average} \n")
Output_file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " ($" + str(greatest_increase) + ")\n")
Output_file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " ($" +str(greatest_decrease) + ")\n")