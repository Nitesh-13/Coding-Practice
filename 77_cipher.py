#

'''

The Caesar cipher is a type of substitution cipher in which each alphabet in the plaintext or messages is shifted by a nuber of places down the alphabet.
For example, with a shift of 1, P would be replaced by Q, Q would become R, and so on...
To pass an encrypted message from one person to another, it is first necessary that both the parties have the 'Key' for the cipher, so that the sender may encrypt and the receiver may decrypt it.
Key is the number of OFFSET to shift the cipher alphabet. Key can have basic shifts from 1 to 25 positions as there are 26 alphabets.
As we are designing custom caesar cipher, in addition to alphabets, we are consiidering numeric digits from 0 to 9. Digits can also be shifted by key places.
For example, if a given text contains any digit with value 5 and key = 2, then 5 will be replaced by 7.

Input:
AdfTu34
1
Output:
BegUv45

Input:
yZ89
2
Output:
aB01 


'''

def encrypt(msg, key):
    encrypted_msg = ''
    for ch in msg:
        if ch.islower():
            ascii = ord(ch)
            if ascii + key > ord('z'):
                ascii = ord('a') + (ascii+key - ord('z')-1)
            else:
                ascii += key
        else:
            ascii = ord(ch)
            if ch.isdigit():
                sum = int(ch) + key
                ascii = sum if sum<=9 else sum-10
                encrypted_msg += str(ascii)
                continue
            elif ascii + key > ord('Z'):
                ascii = ord('A') + (ascii+key - ord('Z')-1)
            else:
                ascii += key
        encrypted_msg += chr(ascii)
    return encrypted_msg

msg = input()
key = int(input())

print(encrypt(msg, key))
