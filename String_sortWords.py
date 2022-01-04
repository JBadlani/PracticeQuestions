'''
Sort words of sentence in ascending order
Input : to learn programming refer geeksforgeeks
Output : geeksforgeeks learn programming refer to

Input : geeks for geeks
Output : for geeks geeks
'''

def sortWords(sentence):
	words = sentence.split(' ')
	words.sort()
	return "".join(sort)

if __name__ == "__main__":
	sentence = "My name is Jaya"
	print(sortWords(sentence))


'''
Note that output here will be 'J' first as it has lower ASCII value than 'j'. 
JayaMyisname
Always check for case in Question - will it be lower case or title format - how we have to return it
'''

