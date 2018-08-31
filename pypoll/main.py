import os
import csv

# Path to collect data from the Resources folder
pollcsv = os.path.join('.', 'Resources', 'election_data.csv')
# Read in the CSV file

with open(pollcsv, 'r') as csvfile:

    # Split the data on commas
    poll = csv.reader(csvfile, delimiter=',')
    
    header = next(poll)
    
    #setting initial value as 0 for counting number for each candidate
    khan=0
    correy=0
    Li=0
    Tooley=0
    
    for row in poll:
        if row[2]=="Khan":
            khan=khan+1
        elif row[2]=="Correy":
            correy=correy+1
        elif row[2]=="Li":
            Li=Li+1
        elif row[2]=="O'Tooley":
            Tooley=Tooley+1
            
    #counting the total number of votes
    Total=khan+correy+Li+Tooley
   
   #Calculating the percentage
    khan_percent=round(khan/Total*100,4)
    correy_percent=round(correy/Total*100 ,4)
    Li_percent=round(Li/Total*100,4)
    Tooley_percent=round(Tooley/Total*100,4)
    
    #selecting the winner
    percent=[khan_percent,correy_percent,Li_percent, Tooley_percent]
    candidate=["Khan","Correy","Li","O'Tooley"]
   
    winner=candidate[percent.index(max(percent))]
    
#output the results to text file
file = open("Poll.txt","w") 
 
file.write("Election Results\n")
file.write("  -------------------------\n") 
file.write(f'Total Votes: {Total}\n')
file.write("  -------------------------\n") 
file.write(f'Khan: {khan_percent}% ({khan})\n') 
file.write(f'Correy: {correy_percent}% ({correy})\n') 
file.write(f'Li: {Li_percent}% ({Li})\n') 
file.write(f'O Tooley: {Tooley_percent}% ({Tooley})\n') 
file.write("  -------------------------\n") 
file.write(f'Winner: {winner}\n') 
file.write("  -------------------------\n") 
file.close()   



#print the results to the terminal 

print("Election Results\n")
print("  -------------------------\n") 
print(f'Total Votes: {Total}\n')
print("  -------------------------\n") 
print(f'Khan: {khan_percent}% ({khan})\n') 
print(f'Correy: {correy_percent}% ({correy})\n') 
print(f'Li: {Li_percent}% ({Li})\n') 
print(f'O Tooley: {Tooley_percent}% ({Tooley})\n') 
print("  -------------------------\n") 
print(f'Winner: {winner}\n') 
print("  -------------------------\n")

        