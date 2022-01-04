'''
Python | Remove all duplicates words from a given sentence.
Input : Geeks for Geeks
Output : Geeks for

Input : Python is great and Java is also great
Output : is also Java Python and great
'''

def removeDupWords(sentence):
	words = sentence.split(' ')
	output = []
	seen = set()
	for word in words:
	    if word not in seen :
	        seen.add(word)
	        output.append(word)
	return "".join(output)

if __name__ == "__main__":
	Input = "Geeks for Geeks"
	print(removeDupWords(Input))