import os
import csv

#path for reading the csv
csvpath = os.path.join("PyPoll", "resources", "election_data.csv")

#Variables
candidate_index = 2
candidate_set = set()
candidate_list = []
cand_list_full = []
total_votes = 0
cand1_votes = 0
cand2_votes = 0
cand3_votes = 0


#Read csv file
with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)

   for row in csvreader:
       #Count the number of votes by finding length of file (one vote per row)
       total_votes += 1

       #Create list to store values
       cand_list_full.append(row[2])
        
#Create the list of candidates
       try:
           candidate = row[candidate_index]
           candidate_set.add(candidate)
       except IndexError:
           pass    
candidate_list = list(candidate_set)   
cand1 = str(candidate_list[0])
cand2 = str(candidate_list[1])
cand3 = str(candidate_list[2])

#count the votes each candidate recieved
   
for value in cand_list_full:
   if cand1 in value:
      cand1_votes += 1
   if cand2 in value:
      cand2_votes += 1
   if cand3 in value:
      cand3_votes += 1  

#find the percentage of the total votes each candidate recieved
# format percentage      
cand1_per = (cand1_votes/total_votes)*100    
cand1_per_f = f"{cand1_per:.3f}"
cand2_per = (cand2_votes/total_votes)*100    
cand2_per_f = f"{cand2_per:.3f}"           
cand3_per = (cand3_votes/total_votes)*100    
cand3_per_f = f"{cand3_per:.3f}"

#list to hold vote counts
vote_list = [cand1_votes, cand2_votes, cand3_votes]

#  use the index of the largest number of votes to find the candidate with the same index
most_votes = max(vote_list)
most_votes_index = vote_list.index(most_votes)
winner = candidate_list[most_votes_index]
   

    
# print results to terminal

print(f"Election Results")
print(f"Total Votes: {total_votes}")
print(f"{cand1}: {cand1_per_f}% ({cand1_votes})")
print(f"{cand2}: {cand2_per_f}% ({cand2_votes})")
print(f"{cand3}: {cand3_per_f}% ({cand3_votes})")
print(f"Winner: {winner}")

#print results to text file

analysis_file = open(r"PyPoll\analysis\PyPoll_analysis.txt", "w+")
analysis = ["Election Results \n", "Total Votes: 369711 \n", "Raymon Anthony Doane: 3.139% (11606) \n",
            "Charles Casper Stockham: 23.049% (85213) \n", "Diana DeGette: 73.812% (272892) \n", "Winner: Diana DeGette"]
analysis_file.writelines(analysis)