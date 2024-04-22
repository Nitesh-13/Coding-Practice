# https://www.geeksforgeeks.org/print-subsequences-string/

'''

Given a string, we have to find out all its subsequences of it. A String is a subsequence of a given String, that is generated by deleting some character of a given string without changing its order.

'''

string = 'hello'

# Subsequence using recursion
def getSubSequence(string, output):
    
    if len(string) == 0:
        return [output] if output else []
    
    sub_with_char = getSubSequence(string[1:], output + string[0])
    sub_without_char = getSubSequence(string[1:], output)
    
    return sub_with_char+sub_without_char

subsequences = getSubSequence(string,"")
print(len(subsequences))
print((2**len(string))-1) # Formula for no. of possible subsequences (2^n-1)

# If we need string subsequences like 'hel', 'hello', pass '' as output
# If we need list as subseqquence like  ['l', 'o'], ['l'], pass [] as output
# If list, modify the sequence[0] to be in the list aswell


# Subsequence with their indexes
def getSubSequenceWithIndices(sequence, output, index = 0):
    
    if len(sequence) == 0:
        return [output] if output else []
    
    sub_with_char = getSubSequenceWithIndices(sequence[1:], output + [(index,sequence[0])], index+1) # Changes here
    sub_without_char = getSubSequenceWithIndices(sequence[1:], output, index+1)
    
    return sub_with_char+sub_without_char