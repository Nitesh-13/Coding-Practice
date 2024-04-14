# https://www.geeksforgeeks.org/program-count-vowels-consonant-digits-special-characters-string/

'''

Given a string and the task is to count vowels, consonant, digits and special character in string. Special character also contains the white space.
Examples: 
 

Input : str = "geeks for geeks121"
Output : Vowels: 5
         Consonant: 8
         Digit: 3
         Special Character: 2

'''

str = input()
vowels = ['a','e','i','o','u']

v, c, d, s = 0,0,0,0

for chr in str:
    if chr.isalpha():
        if chr.lower() in vowels:
            v += 1
        else:
            c += 1
    elif chr.isnumeric():
        d += 1
    else:
        s += 1
        
print(f'Vowels: {v}\nConsonants: {c}\nDigits: {d}\nSpecial Characters: {s}')