# https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/

'''

Given a Roman numeral, the task is to find its corresponding decimal value and vice versa.

'''

roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

integer_to_roman = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


n = input()


def roman_to_integer(n):
    num = 0
    if n in roman_numerals:
        num = roman_numerals[n]
    else:
        str = n[::-1]

        for ind, chr in enumerate(str):
            minus = True
            if ind == 0:
                minus = False
            if (minus and roman_numerals[chr] < roman_numerals[str[ind-1]]):
                num -= roman_numerals[chr]
            else:
                num += roman_numerals[chr]
    return num


def return_min_max(n):
    min, max = 0,0
    for num in integer_to_roman.keys():
        if num > n:
            max = num
        elif num < n:
            min = num

        if min != 0 and max != 0:
            return min, max


n = int(n)

def to_roman(n):
    out = ''

    if n != 1:
        min, max = return_min_max(n)
    if n in integer_to_roman:
        out = integer_to_roman[n]
    elif (max - n) == 1 or (max-n)%5 != 0:
        reverse = False
        if n<10:
            reverse = True
        while n!= 0:
            if n in integer_to_roman:
                out += integer_to_roman[n]
                if reverse:
                    out = out[::-1]
                break
            min, max = return_min_max(n)
            if n > 10:
                n = n - min
                out += integer_to_roman[min]
            else:
                n = max - n
                out += integer_to_roman[max]
    else:
        min, max = return_min_max(n)
        while n != 0:
            n -= min
            out += integer_to_roman[min]

            if n not in integer_to_roman:
                min, _ = return_min_max(n)
            else:
                out += integer_to_roman[n]
                break
    print(out)
        