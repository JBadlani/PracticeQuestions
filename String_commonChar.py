'''
Python code to print common characters of two Strings in alphabetical order.
Input : 
string1 : geeks
string2 : forgeeks
Output : eegks
Explanation: The letters that are common between 
the two strings are e(2 times), k(1 time) and 
s(1 time).
Hence the lexicographical output is "eegks"

Input : 
string1 : hhhhhello
string2 : gfghhmh
Output : hhh
'''

from collections import Counter

def commonChar(string1,string2):
	
	dict1 = Counter(string1)
	dict2 = Counter(string2)
	
	common = dict1&dict2
	
	if len(common) <= 0:
	    return -1
	else:
	    elemen = sorted(list(common.elements()))
	return ("".join(elemen))


# Driver program
if __name__ == "__main__":
	string1 = 'geeks'
	string2 = 'forgeeks'
	print(commonChar(string1,string2))
