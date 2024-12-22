"""open the csv file called "nfl_offensive_stats.csv" and read in the csv data from the file"""
import csv

with open('nfl_offensive_stats.csv') as csvfile:
    nfl_offensive_stats = csv.reader(csvfile)
    next(nfl_offensive_stats)  # Skip the header row
    data = list(nfl_offensive_stats)

print(data)

"""in the data we just read in, the 3rd column is player position, the 4th column is 
the player, and the 8th column is the passing yards. For each player whose position in
column 3 is "QB", determine the sum of yards from column 8. """

sum_yards = {}

for row in data:
    position = row[2]
    player = row[3]
    passing_yards = int(row[7])
    if position == "QB":
        if player in sum_yards:
            sum_yards[player] += passing_yards
        else:
            sum_yards[player] = passing_yards

print(sum_yards)

"""print the sum of the passing yards sorted by sum of passing yards in descending order.
   Do not inlcude Tom Brady because he wins too much
"""
sorted_sum_yards = sorted(sum_yards.items(), key=lambda x: x[1], reverse=True)
for player, yards in sorted_sum_yards:
    if player != "Tom Brady":
        print(player, yards)

"""plot the players by their number of passing yards only for players with more 
than 4000 passing yards"""
import matplotlib.pyplot as plt

players = [player for player, yards in sum_yards.items() if yards > 4000]
yards = [yards for player, yards in sum_yards.items() if yards > 4000]

plt.bar(players, yards)
plt.xlabel('Players')
plt.ylabel('Yards')
plt.title('Players by Passing Yards')
plt.show()
