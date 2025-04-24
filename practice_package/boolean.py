check_between_numbers = lambda A, B, C: (A < B < C) or (C < B < A)

check_odd_three = lambda number: (100 <= abs(number) <= 999) and (number % 2 != 0)

check_unique_digits = lambda number: 100 <= abs(number) <= 999 and len(set(str(abs(number)))) == 3

def check_palindrome_number(number):
    num_str = str(abs(number))
    return num_str == num_str[::-1]

check_ascending_digits = lambda number: 100 <= abs(number) <= 999 and str(abs(number))[0] < str(abs(number))[1] < str(abs(number))[2]
