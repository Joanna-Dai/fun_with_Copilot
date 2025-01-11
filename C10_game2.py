import random
import tkinter as tk
from tkinter import messagebox

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
    # Dummy implementation for demonstration purposes
    correct = sum(1 for g, s in zip(guess, secret_code) if g == s)
    misplaced = len(set(guess) & set(secret_code)) - correct
    return correct, misplaced

def play(num_digits, max_guesses):
    secret_code = '1234'  # Dummy secret code for demonstration purposes

    def check_guess():
        guess = entry.get()
        result = guess_result(guess, secret_code)
        if result[0] == num_digits:
            messagebox.showinfo("Result", "Congratulations! You have found the code.")
            root.quit()
        else:
            result_label.config(text=f'Correct: {result[0]}  Misplaced: {result[1]}')
            guesses_left.set(guesses_left.get() - 1)
            if guesses_left.get() == 0:
                messagebox.showinfo("Result", f'Sorry, you have run out of guesses. The code was {secret_code}.')
                root.quit()

    root = tk.Tk()
    root.title("Guess the Code Game")
    tk.Label(root, text="Enter your guess:").pack()
    entry = tk.Entry(root)
    entry.pack()

    tk.Button(root, text="Submit", command=check_guess).pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    guesses_left = tk.IntVar(value=max_guesses)
    tk.Label(root, textvariable=guesses_left).pack()

    root.mainloop()

if __name__ == '__main__':
    play(4, 10)