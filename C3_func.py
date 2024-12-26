# write a function that returns the larger of the two numbers
# input is two numbers
# output is the larger of the two numbers
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def larger(num1, num2):
    """
    num1 and num2 are two numbers.
    return the larger of the two numbers
    """ 
    if num1 > num2:
        return num1
    else:
        return num2


# call the larger function with the value 3 and 5
# store the result in a variable called result
# then print the result
result = larger(3, 5)
print(result)


def money_made(num_shares, purchase_share_price, current_share_price):
    """
    num_shares is the number of shares purchased
    purchase_share_price is the price of the share when purchased
    current_share_price is the current price of the share

    return the amount of money made if the shares are sold at the current price
    """
    return num_shares * (current_share_price - purchase_share_price)


def is_strong_password(password):
    """
    a strong password has at least one uppercase character,
    at least one number, and at least one punctuation

    return True if the password is a strong password. False if not.
    """
    has_upper = False
    has_number = False
    has_punctuation = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():
            has_punctuation = True

    return has_upper and has_number and has_punctuation


def get_strong_password():
    """
    keep asking user for a password until it is strong password
    and return that strong password
    """
    password = input("Enter a password: ")
    while not is_strong_password(password):
        password = input("Enter a password: ")
    return password

# call get_strong_password() and store the result in a variable called password
password = get_strong_password()


def num_points(word):
    """
    each letter is worth the following points:
    a, e, i, o, u, l, n, s, t, r: 1 point
    d, g: 2 points
    b, c, m, p: 3 points
    f, h, v, w, y: 4 points
    k: 5 points
    j, x: 8 points
    q, z: 10 points

    word is a word consisting of lowercase characters
    return the sum of the points of each letter in the word
    """
    points = 0
    for char in word:
        if char in "aeioulnstr":
            points += 1
        elif char in "dg":
            points += 2
        elif char in "bcmp":
            points += 3
        elif char in "fhvwy":
            points += 4
        elif char in "k":
            points += 5
        elif char in "jx":
            points += 8
        elif char in "qz":
            points += 10
    return points
  
points = num_points("zap")
print(points)


def best_word(word_list):
    """
    word_list a list of words
    return the word with the most points
    """
    best_word = ""
    best_points = 0
    for word in word_list:
        points = num_points(word)
        if points > best_points:
            best_word = word
            best_points = points
    return best_word

# call best_word function with 'zap', 'pack', 'quack'
# store the result in a variable called best
# then print the result
best = best_word(['zap', 'pack', 'quack'])
print(best)