import os
import csv

poll_csv = 'Resources/election_data.csv'

with open(poll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    total_votes=0
    winner=""
    top_results=0
    candidate_list=[]
    candidate_dict={}
    percent_of={}
    for row in csvreader:
       # voter_id = int(poll_csv[0])
        county = str(poll_csv[1])
        candidate = (row[2])


        # count = 0
        # total = 0
        total_votes = total_votes+1
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_dict[candidate]=0
        candidate_dict[candidate]=candidate_dict[candidate]+1
    print(f"Election Results")
    print("--------------------")
    print(f"Total Votes:{total_votes}")
    print("--------------------")
    print(candidate_list)
    print("--------------------")
    for x in candidate_dict:
        percent_of[x]=round(candidate_dict[x]/total_votes*100,2)
        if candidate_dict[x]>top_results:
            top_results=candidate_dict[x]
            winner=x
        print(f":{x}: {percent_of[x]}% ({candidate_dict[x]})")
        

    
    #print(f":{percent_of}{candidate_dict[x]}")
    #print(percent_of)
    print("--------------------")
    print(f"Winner:{winner}")

with open("Election.txt","w+") as f:

    f.write(f"Election Results \n")
    f.write(f"Total Votes:{total_votes}\n")
    f.write(f"{candidate_list}\n")
    f.write(f"{percent_of}\n")
    f.write(f"Winner: {winner}")
    f.close()
    