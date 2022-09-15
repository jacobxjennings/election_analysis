
#Open/load the data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 

#Import the datatime module
import datetime as dt
import csv
import os

#Use the now() attribute on the datatime class to get the present time
now = dt.datetime.now()

#Print the present time
print("The time right now is ",now)

#Assign a variable for the file to load and the path and add a variable to save the file to a path.
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Assign a variable for analysis
total_votes = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Declare a empty lists and dictionaries
candidate_options = []
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reaeer function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        #Print the candidate name for each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        
            #Add the candidate name to the candidatte list.
            candidate_options.append(candidate_name)

            #Beging tracking that candidates vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        #Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

#Print the candidate list
#print(candidate_options)
#print(candidate_votes)
#print(winning_candidate)
#print(votes)
#print(winning_percentage)
        print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------\n")

print(winning_candidate_summary)











