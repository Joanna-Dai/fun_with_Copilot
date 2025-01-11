import random

def random_string(length):
    """
    length is an integer.

    return a string of the given length, where each character
    is a digit from 0 to 9, and with no repeated digits.
    """
    s = ''
    while len(s) < length:
        digit = str(random.randint(0, 9))
        if digit not in s:
            s += digit
    return s



def get_guess(length):
    """
    length is an integer.

    keep asking the player to enter a string where each character
    is a digit from 0 to 9, until they enter a valid guess.
    a valid guess has the given length and has no repeated digits.
    """
    while True:
        guess = input('Enter a {}-digit guess: '.format(length))
        if len(guess) != length:
            print('Your guess must have {} digits.'.format(length))
        elif not guess.isdigit():
            print('Your guess must contain only digits.')
        elif len(set(guess)) != length:
            print('Your guess must not contain repeated digits.')
        else:
            return guess



def guess_result(guess, secret_code):
    """
    guess and secret_code are strings of the same length.

    return a list of two values:
    the first value i the number of inidices in guess where the
    character at that index matches the character at the same 
    index in secret_code.
    the second value is number of indices in guess where the character
    at index exist at a different index in secret_code.
    """
    correct = 0
    misplaced = 0
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            correct += 1
        elif guess[i] in secret_code:
            misplaced += 1
    return [correct, misplaced]



def play(num_digits, num_guesses):
    """
    generate a random string with num_digits digits.
    the player has num_guesses guesses to guess the random string.
    after each guess, the player is told how many digits in the guess
    are in the correct place, and how many digits are in the wrong
    place but in the string.
    """
    secret_code = random_string(num_digits)
    print('I have generated a {}-digit code with no repeated digits.'.format(num_digits))
    print('You have {} guesses to find it.'.format(num_guesses))
    for i in range(num_guesses):
        guess = get_guess(num_digits)
        result = guess_result(guess, secret_code)
        if result[0] == num_digits:
            print('Congratulations! You have found the code.')
            return
        else:
            print('Correct: {}  Misplaced: {}'.format(result[0], result[1]))
    print('Sorry, you have run out of guesses. The code was {}.'.format(secret_code))


if __name__ == '__main__':
    play(4, 10)