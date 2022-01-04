'''
Print number with commas as 1000 separators in Python.
Input : 1000000
Output : 1,000,000

Input : 1000
Output : 1,000

Syntax : " ".format()
Input  : print ('{0}, {1}, {2}'.format('a', 'b', 'c'))
Output : a, b, c
Input :  print ('{2}, {0}, {1}'.format('a', 'b', 'c'))
Output : c, a, b
'''

def place_value(number):
    return "{:,}".format(number)
    
# Driver program
if __name__ == "__main__":
	number = 1000000
	print(place_value(number))