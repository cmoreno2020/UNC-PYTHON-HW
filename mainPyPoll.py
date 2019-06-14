#************************ PYPOLL ******************************

#Import libraries for creating file path and for opening CSV files
import os
import csv

#Create path for election data file
pathf = os.path.join('PyPoll','Resources','election_data.csv')

#candidates = []

#Open file with election data
with open(pathf, newline='') as csvfile:

  # CSV reader with specified delimiter and variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=',')

  # Read the header row first (skip this step if there is now header)
  csv_header = next(csvreader)

  #Initialize variable for calculations and for storing data
  tvotes = 0   #Initialize variable to hold the total votes
  datel = []   #List to hold dates for each row
  valuel = []  #List to hold values for each row
  candidates = []  #List to hold candidates name
  candidatesv = [] #List to hold votes for candidate

  # Read each row of data after the header
  for row in csvreader:

    i = 0
    tvotes += 1  # Add one to total votes (tvotes)
    if row[2] not in candidates:      #If candidate is not in the list of candites
        candidates.append(row[2])     #Add candidate to list of candidates
        candidatesv.append(1)         #Initialize the value of votes for candidate in one
    else:
        candidatesv[candidates.index(row[2])] += 1  #If candidate is already on list, increment votes for candidate by one

percentage = []
winner =""
maxv = 0

#To calculate % of total for candidates and to present data in screen

print ("------------------------------------")
print ("Total Votes: ",tvotes)
print ("------------------------------------")

#Go through list of candidate data to calculate percentage of total to be stored in percentage list
for i in range (len(candidatesv)):
    percentage.append((candidatesv[i]/tvotes)*100)   # Calculate % of total for candidate and store it in percentage list
    print(candidates[i],": {:0,.3f}".format(percentage[i]),"% (",candidatesv[i],")")  #Print information on the screen

    # Identify the candidate with highest number of votes
    if candidatesv[i] > maxv:
      maxv = candidatesv[i]
      winner = candidates[i]

print ("------------------------------------")
print ('Wineer is: ', winner)   #Print information for the winner
print ("------------------------------------")

# Output file path
output_file = os.path.join("outputPyPoll.csv")

# open the output file, and write summary information for votes per candidate
with open(output_file, "w", newline="") as datafile:
  writer = csv.writer(datafile)
  writer.writerow(["-------------------------"])
  writer.writerow (["Total Votes: " + str(tvotes)])
  writer.writerow (["------------------------------------"])
  for i in range (len(candidatesv)):
    writer.writerow([candidates[i] + ": "+ str(round(percentage[i],1)) + "% (" + str(candidatesv[i]) + ")" ])
  writer.writerow (["------------------------------------"])
  writer.writerow (['Wineer is: ' + winner])
  writer.writerow (["------------------------------------"])



"""

Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  """