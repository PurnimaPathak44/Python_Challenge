#Dependencies
import os
import csv

#Specifying the file to read from
csvpath = os.path.join('Resources', 'budget_data.csv')

#Setting up variables
months= set()
revenue= list()
diff = list()
dates=[]
prev_revenue = None


# #open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# skipping header
    next(csvreader, None)
#Traverse the entire loop
    for row in csvreader:

#adding months to month set
        months.add(row[0])

#adding months to total list
        revenue.append((int(row[1])))

#ASSIGNING RECENT REVENUE
        dates.append(row[0])
        current_revenue=int(row[1]) 

# to skip first data and adding difference to Diff list
        if (prev_revenue is not None): 
            diff.append(current_revenue-prev_revenue)


        prev_revenue=current_revenue # as current revenue will be prev revenue in next iteration of loop
no_of_months=len(months)
total=sum(revenue)
average_change=sum(diff)/len(diff)
incr_profit=max(diff)
decr_profit=min(diff)
i=diff.index(incr_profit)
j=diff.index(decr_profit)
        
    

#Printing the calculated analysed results

print("total months :", no_of_months)
print("total:","$", total)
print("Average Change:", "$", round(average_change, 2))
print("Increase_Profit", "$",dates[i+1], incr_profit)
print("Decrease_Profit", "$",dates[j+1], decr_profit)



# Specifying the file to write to 

outputpath= os.path.join('AnalysisPyBank', 'MainPyBank.txt')

with open(outputpath, 'w')as file:

#Writing the results in a file
    file.write("Financial Analysis \n_______________________________________\n")
    file.write(f"total months :{no_of_months} \n_______________________________________\n")
    file.write(f"total: $ {total} \n_______________________________________\n")
    file.write(f"Average Change: {round(average_change, 2)} \n")
    file.write(f"Increase_Profit: {dates[i+1], incr_profit} \n")
    file.write(f"Decrease_Profit: {dates[j+1], decr_profit} \n_______________________________________\n")





