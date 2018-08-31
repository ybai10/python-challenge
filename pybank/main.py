import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('.', 'Resources', 'budget_data.csv')
# Read in the CSV file

with open(budgetCSV, 'r') as csvfile:
    # Split the data on commas
    budget = csv.reader(csvfile, delimiter=',')

  # Read each row of data after the header
    header = next(budget)
     
    #setting the initial value at record=0 to count the total number of rows
    record=0
    #setting the initial value at total=0 to calculate the total net amount of profit/loss
    total=0

    #creating list  profitloss to store profit/loss
    profitloss=[]
    #creating list month to store months
    month=[]
    #creating list to store the net change between months, the length of this list is (n-1)
    change=[]
    
    for row in budget:
        if len(row)==0:
            record=record+0
        else: 
            record=record+1
            
        total=total+int(row[1])
        profitloss.append(int(row[1]))
        month.append(row[0])
        
   
    for y in range(len(profitloss)-1):
        change.append( profitloss[y+1]- profitloss[y])
        avg=sum(change)/len(change)
        
    great=max(change)
    worst=min(change)
    great_month=month[change.index(max(change))+1]
    worst_month=month[change.index(min(change))+1]   



#output the results to text file
file = open("bank.txt","w") 
 
file.write("Financial Analysis\n")
file.write(" -----------------------------------------\n") 
file.write(f'Total Month: {record}\n')
file.write(f'Total: {total}\n')
file.write(f'Average  Change: {avg}\n')
file.write(f'Greatest Increase in Profits: {great_month} (${great})\n')
file.write(f'Greatest Decrease in Profits: {worst_month} (${worst})\n')
 
file.close() 


#print the results to the terminal 

print("Financial Analysis\n")
print(" -----------------------------------------\n") 
print(f'Total Month: {record}\n')
print(f'Total: {total}\n')
print(f'Average  Change: {avg}\n')
print(f'Greatest Increase in Profits: {great_month} (${great})\n')
print(f'Greatest Decrease in Profits: {worst_month} (${worst})\n')
