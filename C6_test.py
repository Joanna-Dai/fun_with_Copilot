
def longest_word(words):
    """
    word is a list of words
    
    return the word from the list with the most characters
    if multiple words are the longest, return the first one

    >>> longest_word(["happy", "birthday", "my", "friend"])
    'birthday'

    >>> longest_word(["happy"])
    'happy'

    >>> longest_word(['',''])
    ''
    """

    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# main that performs the test
import doctest
doctest.testmod(verbose=True)