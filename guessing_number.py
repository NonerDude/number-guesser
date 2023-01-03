from __future__ import annotations
from typing import Tuple

import config as conf

import random
import string
import re



def build_count_base_digits(count_base):
    return string.digits[:min(count_base, conf.DIGITS_COUNT_BASE)] + string.ascii_uppercase[:max(count_base - conf.DIGITS_COUNT_BASE, 0)]


def format_count_base_range(count_base):
    return f'([0-{min(count_base, 9)}]{"[A" if count_base > conf.DIGITS_COUNT_BASE else ""}' \
           f'{f"-{string.ascii_uppercase[count_base - conf.DIGITS_COUNT_BASE - 1]}]" if count_base > conf.DIGITS_COUNT_BASE + 1 else ""})'


class GuessingNumber:
    @staticmethod
    def _has_duplicates(number):
        return any(number[i] in number[i+1:] for i in range(len(number)))
        
    def __init__(self, number, count_base, digits_amount):
        if not digits_amount == len(number):
            raise ValueError(f'Number should have {digits_amount} digits')

        if GuessingNumber._has_duplicates(number):
            raise ValueError(f'Number can\'t have duplicate digits')

        if not re.fullmatch(f'[0-9{"A-" if count_base > 10 else ""}'
                            f'{string.ascii_uppercase[count_base - conf.DIGITS_COUNT_BASE - 1] if count_base > conf.DIGITS_COUNT_BASE + 1 else ""}' + ']*',
                            number):
            raise ValueError(f'Number digits should be in range {format_count_base_range(count_base)}')
        self.number = number
        self.count_base = count_base
        self.digits_amount = digits_amount
        
    
    def _generate_number(count_base, digits_amount):
        return ''.join(random.sample(string.digits[:count_base] + string.ascii_uppercase[:max(0, count_base-conf.DIGITS_COUNT_BASE)], digits_amount))

    @staticmethod
    def check(guess, number):
        in_place, wrong_place = 0, 0
        for i in range(len(guess)):
            if guess[i] == number[i]:
                in_place += 1
            elif guess[i] in number:
                wrong_place += 1
        return in_place, wrong_place

    def compare(self, guessing_number: str) -> Tuple[int]:
        return self.check(guessing_number, self.number)
