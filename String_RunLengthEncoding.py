'''
Run Length Encoding in Python

Input  :  str = 'wwwwaaadexxxxxx'
Output : 'w4a3d1e1x6'
'''

from collections import OrderedDict
def runLengthEncoding(input1):
    dict1 = OrderedDict.fromkeys(input1,0)
    for ch in input1:
        dict1[ch] += 1
    output = ''
    for key,value in dict1.items():
        output += key+str(value)
    return output
    
    
# Driver program
if __name__ == "__main__":
	input1 = 'wwwwaaadexxxxxx'
	print(performOper(input1))

