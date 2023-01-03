


DIGITS_COUNT_BASE = 10
ALPHABET_COUNT_BASE = 26


DEFAULT_COUNT_BASE = 10
MAX_COUNT_BASE = 16
MIN_COUNT_BASE = 6

AMOUNT_OF_CHARS_NOT_IN_NUMBER = 4
DEFAULT_DIGITS_AMOUNT = 5
MIN_DIGITS_AMOUNT = 3
MAX_DIGITS_AMOUNT = MAX_COUNT_BASE - AMOUNT_OF_CHARS_NOT_IN_NUMBER

if 36 <= MAX_COUNT_BASE:
    raise Exception('Max count base out of range')

if not MIN_DIGITS_AMOUNT <= DEFAULT_DIGITS_AMOUNT <= MAX_DIGITS_AMOUNT:
    raise Exception('Default digits amount out of range')


if not MIN_COUNT_BASE <= DEFAULT_COUNT_BASE <= MAX_COUNT_BASE:
    raise Exception('Default count base out of range')