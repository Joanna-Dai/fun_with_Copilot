# Authorship Identification (top-down design + bottom-up implementation)

import string

def clean_word(word):
    '''
    word is a string.

    return a version o word in which all letters have been converted
    to lowercase, and punctuation characters have been removed from
    both ends. inner punctuation characters are left untouched. 
    
    >>> clean_word('Pearl!')
    'pearl'
    >>> clean_word('card-board')
    'card-board'

    '''
    word = word.lower()
    word = word.strip(string.punctuation)
    
    return word



def average_word_length(text):
    '''
    text is a string of text.

    return the average word length of the words in text.
    do not count empty word as words.
    do not include surrounding punctutation.

    >>> average_word_length('A pearl! Pearl! Lustrous pearl! \
        Rare. What a nice find.')
    4.1

    '''

    import string
    text = text.split()
    total = 0
    count = 0
    for word in text:
        word = clean_word(word)
        if word != '':
            total += len(word)
            count += 1
    
    return total / count


def different_to_total(text):
    '''
    text is a string of text.

    return the number of unique words in text
    divided by the total number of words in text.
    Do not count empty words as words.
    Do not include surrounding punctuation.

    >>> different_to_total('A pearl! Pearl! Lustrous pearl! \
        Rare. What a nice find.')
    0.7
        
    '''
    text = text.split()
    total = 0
    unique = []
    for word in text:
        word = clean_word(word)
        if word != '':
            total += 1
            if word not in unique:
                unique.append(word)
    
    return len(unique) / total


def exactly_once_to_total(text):
    '''
    text is a string of text.

    return the number of words that show up exactly once in text
    divided by the total number of words in text.
    Do not count empty words as words.
    Do not include surrounding punctuation.

    >>> exactly_once_to_total('A pearl! Pearl! Lustrous pearl! \
        Rare. What a nice find.')
    0.5

    '''
    text = text.split()
    total = 0
    unique = set()
    once = set()
    for word in text:
        word = clean_word(word)
        if word != '':
            total += 1
            if word in unique:
                once.discard(word)
            else:
                unique.add(word)
                once.add(word)

    return len(once) / total



def split_string(text, separators):
    '''
    text is a string of text.
    separators is a string of separator characters.

    split the text into a list using any of the one-charactor seperators
    and return the result.
    remove spaces from begining and end of a string before adding it to the list.
    do not include empty strings in the list.

    >>> split_string('one*two[three', '*[')
    ['one', 'two', 'three']
    >>> split_string('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    ['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', 'What a nice find']

    '''
    words = []
    word = ''
    for char in text:
        if char in separators:
            word = word.strip()
            if word != '':
                words.append(word)
            word = ''
        else:
            word += char
    
    word = word.strip()
    if word != '':
        words.append(word)
    
    return words