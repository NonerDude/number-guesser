import string
import config as conf
from guessing_number import GuessingNumber, format_count_base_range




def input_count_base():
    count_base = None
    while count_base is None:
        try:
            count_base = input(f'Counting Base ({conf.MIN_COUNT_BASE}-{conf.MAX_COUNT_BASE}, {conf.DEFAULT_COUNT_BASE} default) '
                               f'{format_count_base_range(conf.MAX_COUNT_BASE)}: ')
            if '' == count_base:
                count_base = conf.DEFAULT_COUNT_BASE
                break
            count_base = int(count_base)
            if not conf.MIN_COUNT_BASE <= count_base <= conf.MAX_COUNT_BASE:
                raise ValueError
        except ValueError:
            count_base = None
            print('Please enter a valid counting base.')
    return count_base


def input_digits_amount(count_base):
    digits_amount = None
    while digits_amount is None:
        try:
            digits_amount = input(f'Digits Amount ({conf.MIN_DIGITS_AMOUNT}-{count_base}, {conf.DEFAULT_DIGITS_AMOUNT} default): ')
            if '' == digits_amount:
                digits_amount = conf.DEFAULT_DIGITS_AMOUNT
                break
            digits_amount = int(digits_amount)
            if not conf.MIN_DIGITS_AMOUNT <= digits_amount <= count_base:
                raise ValueError
        except ValueError:
            digits_amount = None
            print('Please enter a valid digits_amount.')
    return digits_amount

def input_number(count_base, digits_amount):
    number = None
    while number is None:
        try:
            number = input(f'Your number {format_count_base_range(count_base)} * '
                           f'{digits_amount} (default: randomly generated): ')
            if '' == number:
                number = GuessingNumber._generate_number(count_base, digits_amount)
                break
        except ValueError as error:
            number = None
            print('Please enter a valid number.', error)
    return GuessingNumber(number, count_base, digits_amount)

def input_guessing_number():
    count_base = input_count_base()
    print("Selected Count Base: ", count_base, format_count_base_range(count_base), '\n')
    digits_amount = input_digits_amount(count_base)
    print("Selected Number Length: ", digits_amount, '\n')
    number = input_number(count_base, digits_amount)
    print("Selected Number: ", number.number, '\n')
    return number