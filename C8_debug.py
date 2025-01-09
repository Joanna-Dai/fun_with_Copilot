def count_words(words):
    count = 0
    for word in words:
        # only count words that are exactly "Dan" (case-sensitive)
        if word == 'Dan':
            count += 1
    return count

words = ['Dan', 'dangerous','Leo']
print(count_words(words))
