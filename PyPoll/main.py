import os
import csv

poll_csv = 'Resources/election_data.csv'

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        voter_id = int(poll_csv[0])
        county = str(poll_csv[1])
        candidate = str(poll_csv[2])


        count = 0
        total = 0
        total_votes = len(poll_csv[0])
        

        print(f"Election Results")
        print("--------------------")
        print(f"Total Votes:{total_votes}")
        print("--------------------")
        print({top_results1})
        print("--------------------")
        print("Winner:{winning_candidate}")

touch(poll_data)
    print(f"Election Results")
    print("--------------------")
    print(f"Total Votes:{total_votes}")
    print("--------------------")
    print({top_results1})
    print("--------------------")
    print("Winner:{winning_candidate}")