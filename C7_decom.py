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



def get_sentence(text):
    """
    text is a string of text.

    return a list o the setences from text. 
    sentences are seperated by '.', '!', or '?'.

    >>> get_sentence('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    ['A pearl', ' Pearl', ' Lustrous pearl', ' Rare', ' What a nice find']

    """
    return split_string(text, '.!?')



def average_sentence_length(text):
    """
    text is a string of text.

    return the average number of words per sentence in text.
    do not count empty wrds as words.

    >>> average_sentence_length('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    2.0

    """
    sentences = get_sentence(text)
    total = 0
    count = 0
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            word = clean_word(word)
            if word != '':
                total += 1
        count += 1
    
    return total / count



def get_phrases(sentence):
    """
    sentence is a sentence string.

    return a list of the phrases from sentence.
    phrases are seperated by ',' or ';' or ':'.

    >>> get_phrases('A pearl, Pearl; Lustrous pearl: Rare.')
    ['A pearl', ' Pearl', ' Lustrous pearl', ' Rare']

    """
    return split_string(sentence, ',;:')



def average_sentence_complexity(text):
    """
    text is a string of text.

    return the average number of phrases per sentence in text.

    >>> average_sentence_complexity('A pearl! Pearl! Lustrous pearl! Rare.\
        What a nice find.')
    1.0

    >>> average_sentence_complexity('A pearl! Pearl! Lustrous pearl! Rare, \
        what a nice find.')
    1.25

    """
    sentences = get_sentence(text)
    total = 0
    count = 0
    for sentence in sentences:
        phrases = get_phrases(sentence)
        for phrase in phrases:
            total += 1
        count += 1
    return total / count



def make_signature(text):
    """
    the signature for text is a list of five elements.
    average word length, different words to total words, \
    words used exactly once to total words, average sentence length, \
    average sentence complexity.

    return the signature for text.

    >>> make_signature('A pearl! Pearl! Lustrous pearl! Rare, What a nice find.')
    [4.1, 0.7, 0.5, 2.5, 1.25]
    
    """
    return [average_word_length(text), different_to_total(text), \
            exactly_once_to_total(text), average_sentence_length(text), \
            average_sentence_complexity(text)]



def get_all_signature(known_dir):
    """
    known_dir is the name of a directory of books.
    for each file in directory known_dir, determine its signature.

    return a dictionary where each key is
    the name of a file, and the value is its signature.

    """
    import os
    signatures = {}
    for file in os.listdir(known_dir):
        with open(known_dir + '/' + file, 'r') as f:
            text = f.read()
            signatures[file] = make_signature(text)
    
    return signatures
