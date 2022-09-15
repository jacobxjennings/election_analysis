
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

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reaeer function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)






# with open(file_to_save,"w") as txt_file:

#     #Write three counties to the file
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("_______________________________\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")










