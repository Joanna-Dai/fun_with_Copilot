
def tot_pass_yds_player(input_file, player):
    """
    input_file is a string that is the name of a file
    player is a string that is the name of a player

    the file is a csv file with a header row
    column 4 is the player's name
    column 8 is the number of passing yards for that player

    return the total number of passing yards for the player

    >>> tot_pass_yds_player('nfl_offensive_stats.csv', 'Aaron Rodgers')
    13852
    >>> tot_pass_yds_player('nfl_offensive_stats.csv', 'Patrick Mahomes')
    16132
    >>> tot_pass_yds_player('nfl_offensive_stats.csv', 'Leo Porter')
    0

    """
    import csv
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        total = 0
        for row in reader:
            if row[3] == player:
                total += int(row[7])
    
    return total


# perform the tests
import doctest
doctest.testmod(verbose=True)