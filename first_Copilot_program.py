# output "Hello Copilot" to the screen
print("Hello Copilot")

"""open the csv file called "nfl_offensive_stats.csv" and read in the csv data from the file"""
import csv
with open('nfl_offensive_stats.csv') as csvfile:
    nfl_offensive_stats = csv.reader(csvfile)
    for row in nfl_offensive_stats:
        print(row)

"""in the data we just read in, the 4th column is the player and the 8th column is the playing yards. 
get the sum of yards from column 8 where the 4th column is "Aaron Rodgers" """
with open('nfl_offensive_stats.csv') as csvfile:
    nfl_offensive_stats = csv.reader(csvfile)
    sum_yards = 0
    for row in nfl_offensive_stats:
        if row[3] == "Aaron Rodgers":
            sum_yards += int(row[7])
    print(sum_yards)




