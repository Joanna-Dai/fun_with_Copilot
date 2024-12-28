
def most_students(classroom):
    """
    classroom is a list of lists
    each ' ' is an empty seat
    each 'S' is a student
    
    return the maximum total number of ' ' characters in a given row

    >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], \
                      ['S', 'S', 'S', 'S', 'S', 'S'], \
                      [' ', 'S', ' ', 'S', ' ', ' ']])
    4
    
    >>> most_students([['S','S','S'],\
                       ['S','S','S'],\
                       ['S','S','S']])
    0
         
    """ 
    most = 0
    for row in classroom:
        count = 0
        for seat in row:
            if seat == ' ':
                count += 1
        if count > most:
            most = count

    return most

# main that performs the test
import doctest
doctest.testmod(verbose=True)