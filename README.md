# Election Analysis
## Overview
Throughout this project, I was tasked with auditing the results of an election from a CSV file that was provided. Using Python, I was able to sort through the dataset to tally results and output different analytics. Python was picked for this project due to the large amount of data that is being handled. 

## Results
* After importing the CSV file into Python I was able to iterate through every row in the dataset after the header by simply adding one each row:

    `reader = csv.read(election_data)
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
    print(total_votes)`

* To determine the total number of votes and the percentagee of total votes for each county you must first figure out how many counties were involved in this election. Therefore, you must create a new list and set it equal to zero. This list is called **county_names**. Then to interate through the data, adding county to the list with the condition that the county_name is not in **county_names**. While it does that, it also compiles votes that correspond to the county and is stored as a dictionary called **votes_per_county**. 

    'county_names = []
	votes_per_county = {}
	    for row in reader:
		    if county_name not in county_names:
		        county_names.append(county_name)
		        votes_per_county[county_name] = 0
            votes_per_county[county_name] += 1

        county_votes = votes_per_county[county]
		for county in county_names:
	        county_votes = votes_per_county[county]
    	    county_percentage = '{:.1%}'.format(county_votes / total_votes)
	        print(f"{county}: {county_percentage} ({county_votes:,})")'

* To determine which county had the largest number of votes, you use the following conditional statement: 

    `if (county_votes > winning_county_count):
        winning_county = county
    print(f"Largest County Turnout: {winning_county}")`

* Like the previously point, you do the following to determine the number of votes peer candidate:

    `candidate_results = (
	            f"\nVotes Per Candidate:\n"
	    for candidate_name in candidate_votes:
	        votes = candidate_votes.get(candidate_name)
	        vote_percentage = float(votes) / float(total_votes) * 100
	        candidate_results += (
	            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
	        if (votes > winning_count) and (vote_percentage > winning_percentage):
	            winning_count = votes
	            winning_candidate = candidate_name
	            winning_percentage = vote_percentage
	    print(candidate_results)`

* To determine which candidate won the election you simply print a winning summary based on **winning_candidate**, **winning_count**, and **winning_percentage** from the code above. 

    `   Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%`

## Summary
The good thing this particular scripts and scripts like it is that it shouldn't need any modifications to run other data samples **as long as** the data is formatted the same as **election_results.csv**. To avoid this, improvements could be made to make the script more dynamic with different datasets. For example:

* The script could dynamically determine the order of columns incase future datasets change. I am not quite sure how this could be done but maybe it could connect to an API that provides county across the county to determine county as a specific column. 

* Future data might not provide a header so we could use an if statement with keywords in a list to determine if row[0] is a heading or not. If one or more keywords match it could run **header = next(reader)** if false, it would skip that. 

Lastly, we could implement the exporation of CSV and change the script to have the user import which type of file export they would like. 