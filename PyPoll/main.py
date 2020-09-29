import os
import csv

poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

Total Votes = []
Winner = []

with open(poll_csv as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

for row in csvreader:
        print(row)
