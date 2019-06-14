#*********************  PYBANK *************************************

#Import libraries for creating file path and for opening CSV files
import os
import csv

#Create paht to csv file with budget data
pathf = os.path.join('PyBank','Resources','budget_data.csv')

#Opent csv file, and assign to csvfile
with open(pathf, newline='') as csvfile:
  
  # CSV reader with specified delimiter and variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=',')

  # Read the header row first (skip this step if there is now header)
  csv_header = next(csvreader)

  # Initialize variables to hold the number of observations (months), total sum (tsum), list of values (valuel), and list of associated dates (datel)
  nmonths = 0
  tsum = 0
  datel = []
  valuel = []

  # Read each row of data after the header
  for row in csvreader:

      nmonths += 1                    #increment counter to count the number of observations
      datel.append(row[0])            #Add the date of current row
      valuel.append(float(row[1]))    #Add the value of current row (convert from string to float)
      tsum += float(row[1])           #Add the row value to total value (tsum)

# Create list to hold the calculation for observation to observation change
changes = []

# Initialize variables to hold the minimun change (minv and imin) and the maximum change (maxv and imax). 
# Initialize tchange to hold the summation of changes

minv = 0
maxv = 0
imin = 0
imax = 0
tchange = 0

#Iterate values to calculate changes
for i in range(nmonths):
  
  x = valuel[i]  # Store current value in x

  if i < nmonths-1: # Do calculations only if row is not the last one

     y = valuel[i+1]  # Store value of next value in y
     dif = y-x        # Calculate difference in values (x - y)

     if dif < minv:  # Identify what is the Greatest Decrease (value and location in list)
       minv = dif
       imin = i

     if dif > maxv:  # Identify the Greatest Increase (value and location in list)
       maxv = dif
       imax = i

     changes.append(dif)  #Add the current change to list including them (changes)
     tchange += dif       #Add current change to the total change (tchange)

changes.append(0)      #Add zero (0) to changes to represent the last value 

average = tchange/(nmonths-1) # Calculate the average change

#Print the Financial Anlyst - summary
print ("Financial Analysis:")
print ("---------------------------------")
print ("Total Months: ", nmonths)
print ("Total: ${:0,.2F}".format(tsum))
print ("Average Change ${:0,.2f}".format(average))
print ("Greatest increase in Protits: ",datel[imax+1]," (${:0,.0f})". format(maxv))
print ("Greatest decreasae in Profits: ", datel[imin+1]," (${:0,.0f})".format(minv))

# Create the output file path
output_file = os.path.join("outputPyBank.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:

# Write financial sumamry to file
  writer = csv.writer(datafile)
  writer.writerow(["Financial Analysis:"])
  writer.writerow(["-------------------------"])
  writer.writerow(["Total Months: " + str(nmonths)])
  writer.writerow(["Total: $" + str(tsum)])
  writer.writerow(["Average Change $" + str(average)])
  writer.writerow(["Greatest increase in Protits: " + str(datel[imax+1]) + " ($" + str(maxv) + ")"])
  writer.writerow(["Greatest decreasae in Profits: " + str(datel[imin+1]) + " ($"+ str(minv) + ")"])


"""
EXAMPLE OUTPUT:
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""

