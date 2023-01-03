import os

from input import input_guessing_number
from guesser import RandomOptionGuesser, NextBestGuessGuesser
from itertools import zip_longest

def main():
    print()
    number = input_guessing_number()
    random_option_guesser = RandomOptionGuesser(number.count_base, number.digits_amount, number.compare)
    next_best_guess_guesser = NextBestGuessGuesser(number.count_base, number.digits_amount, number.compare)
    for guess_trial, (guess, result) in enumerate(zip_longest(random_option_guesser.guess(), next_best_guess_guesser.guess(), fillvalue=('-'*number.digits_amount, ('-', '-')))):
        print(guess_trial, guess, result)

    os.system("pause")


if __name__ == '__main__':
    main()
