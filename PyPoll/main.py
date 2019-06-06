import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('..', 'PyPoll', 'election_data.csv')


total_votes = 0
candidates = []
candidate_count = []

#read the csv file
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #This is the total votes cast, just count rows
        total_votes += 1

        candidate = (row[2])
        if candidate in candidates:
            candidate_name = candidates.index(candidate)
            candidate_count[candidate_name] = candidate_count[candidate_name] + 1
        else:
            candidates.append(candidate)
            candidate_count.append(1)
    

    percent= []
    max_votes = candidate_count[0]
    max_index = 0

    for x in range(len(candidates)):
        vote_percent = round((candidate_count[x]/total_votes*100),3)
        percent.append(float(vote_percent))
        
        if candidate_count[x] > max_votes: 
            max_votes = candidate_count[x]
            max_index = [x]
    
    
    Winner = candidates[max_index]
    
        

#Print Results


print("Election Results")
print("......................................................")
print(f"Total Votes: {total_votes}")
print("......................................................")
for x in range(len(candidates)):
    print(f"{candidates[x]} : {percent[x]}% ({candidate_count[x]})")
print("......................................................")
print(f"Election Winner: {Winner}")



#Output File

Output_file = open("PyPoll_Election_Results.txt","w")
            
Output_file.write("Election Results\n")
Output_file.write("............................................\n")
Output_file.write(f"Total Votes: {total_votes}\n")
Output_file.write("............................................\n")
for x in range(len(candidates)):
    Output_file.write(f"{candidates[x]} : {percent[x]}% ({candidate_count[x]})\n")
Output_file.write("............................................\n")
Output_file.write(f"Election Winner: {Winner}\n")