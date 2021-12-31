'''
Find all duplicate characters in string
Given a string, find all the duplicate characters which are similar to each others.
Let’s look at the example.
Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s
'''

from collections import Counter
def charcount(input):
    dict = Counter(input)
    output = []
    for i,j in dict.items():
        if j>1:
            output.append(i)
    return output

# Driver program 
if __name__ == "__main__": 
    input ='GEEFORGEEKSKS'
    print(charcount(input))
