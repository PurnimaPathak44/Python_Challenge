#Dependencies
import os
import csv

#Specifying the file to read 
csvpath= os.path.join("Resources", "election_data.csv")

#Specifying the file to write to
outputpath= os.path.join('AnalysisPyPoll', 'MainPypoll.txt')

#Declaring names as dictionary
names = {}

#Declaring count as Variable to count number of datas
count = 0
with open(outputpath, 'w') as text:

#Opening file
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')


# Skipping Header
        next(csvreader, None)

#Creating loop to access each rows

        for row in csvreader:
# increasing count variable
            count = count+1
# Creating name variable to store Candidates name
            name = row[2]
# Checking if name is in names dictionary
            if name in names:

#Incrementing the value of respective key that is name by 1

                names[name] = names[name]+1

# assigning value 1 if key already exists in dictionary
            else:
                names[name] = 1

# printing and writing the total votes 
    print("total votes",count)
    text.write("Election Results \n__________________________________ \n")
    text.write(f"total votes :{count} \n__________________________________ \n")

# Looping each item in dictionary
    for name,c in names.items():

# Calculating the percentage and printing and writing it.
        percent=(c/count)*100

        print(name,":",round(percent,3),"%",c)
        text.write(f"{name +', ' + str(round(percent,3))}")
        text.write(f"%, {c} \n")

# Finding the key which has maximum value

    max_vote = max(names,key=lambda k:names[k])
    print("winner:",max_vote) 
    text.write("__________________________________\n")
    text.write(f"winner: {max_vote} \n")
    text.write("__________________________________\n")







    
    
    






