'''
K’th Non-repeating Character in Python using List Comprehension and OrderedDict
Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o

Input : str = geeksforgeeks, k = 4
Output : Less than k non-repeating
         characters in input.
'''

from collections import OrderedDict
def findKthuncommon(str1,k):
    dict = OrderedDict.fromkeys(str1,0)
    for ch in dict:
        dict[ch] += 1
    
    nonrepeatdict = [key for key,value in dict.items() if value == 1]
    
    if len(nonrepeatdict) < k:
        return('Less than k non-repeating characters in input ')
    else:
        return nonrepeatdict[k-1]
    
if __name__ == "__main__":
    str1 = 'geeksforgeeks'
    k = 3  
    print(findKthuncommon(str1,k))