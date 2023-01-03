from guessing_number import GuessingNumber, build_count_base_digits
import itertools
import random


class RandomOptionGuesser:
    def __init__(self, count_base, digits_amount, check_guess) -> None:
        self.count_base = count_base
        self.digits_amount = digits_amount
        self.check_guess = check_guess
        self.options = self._init_options()

    
    def _init_options(self):
        for combination in itertools.permutations(build_count_base_digits(self.count_base), self.digits_amount):
            yield ''.join(combination)

    def filter_options(self, guess, result):
        for option in list(self.options):
            if GuessingNumber.check(guess, option) == result:
                yield option

    def guess(self):
        guess = GuessingNumber._generate_number(self.count_base, self.digits_amount)
        result = self.check_guess(guess)
        self.options = list(self.filter_options(guess, result))
    
        while result != (self.digits_amount, 0):
            yield guess, result

            guess = random.choice(self.options)
            result = self.check_guess(guess)
            self.options = list(self.filter_options(guess, result))
        yield guess, result




class NextBestGuessGuesser:
    def __init__(self, count_base, digits_amount, check_guess) -> None:
        self.count_base = count_base
        self.digits_amount = digits_amount
        self.check_guess = check_guess
        self.options = self._init_options()

    def _guesses(self):
        for combination in itertools.combinations_with_replacement(build_count_base_digits(self.count_base), self.digits_amount):
            yield ''.join(combination)
    
    def _init_options(self):
        for combination in itertools.permutations(build_count_base_digits(self.count_base), self.digits_amount):
            yield ''.join(combination)

    def filter_options(self, guess, result):
        for option in list(self.options):
            if GuessingNumber.check(guess, option) == result:
                yield option

    def get_guess_option_reduction_length(self, guess, option):
        return len(list(self.filter_options(guess, GuessingNumber.check(guess, option))))

    def get_guess_options_reduction_length(self, guess):
        return sum(self.get_guess_option_reduction_length(guess, option) for option in list(self.options))


    def best_guess(self):
        return min(self.options, key=lambda guess: self.get_guess_options_reduction_length(guess))
                

    def guess(self):
        guess = GuessingNumber._generate_number(self.count_base, self.digits_amount)
        # guess = '15820'
        result = self.check_guess(guess)
        self.options = list(self.filter_options(guess, result))
    
        while result != (self.digits_amount, 0):
            yield guess, result

            guess = self.best_guess()
            result = self.check_guess(guess)
            self.options = list(self.filter_options(guess, result))
        yield guess, result



  
    # def merge_options(self, options):
    #     self.options
    
    # def  


# NOT_IN_NUMBER = 0
# IN_PLACE = 1
# WRONG_PLACE = 2

# def _gueessing_method_2():
#     perms = set(itertools.permutations([IN_PLACE] * in_place_amount +
#                                        [WRONG_PLACE] * wrong_place_amount +
#                                        [NOT_IN_NUMBER] * (digits_amount - in_place_amount - wrong_place_amount)))
#     print(perms)
#     for perm in perms:
#         in_place = []
#         wrong_place = []
#         not_in_number = []
#         for digit in range(len(perm)):
#             if IN_PLACE == perm[digit]:
#                 in_place.append((guess[digit], digit))
#             if WRONG_PLACE == perm[digit]:
#                 wrong_place.append((guess[digit], digit))
#             if NOT_IN_NUMBER == perm[digit]:
#                 not_in_number.append(guess[digit])
#         options.append((in_place,
#                         wrong_place,
#                         not_in_number))




