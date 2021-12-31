''' 
    Python | Check if there are K consecutive 1’s in a binary number
    Given K and a binary number, check if there exists k consecutive 1’s in the binary number.

    Examples:
    Input : binary number = 101010101111 k = 4 
    Output : yes
    Explanation: at the last 4 index there exists 4 consecutive 1's
    
    Input : binary number = 11100000 k=5 
    Output : no
    Explanation: There is a maximum of 3 consecutive 1's in the given binary.
'''

def binaryCheck(binary,k):
    binary = str(binary)
    i = 0
    count = 0
    while i <= len(binary)-1:
        if binary[i] == '1':
            count+= 1
        else:
            count = 0
        i += 1
        if count >= k:
            return(str(k) + " consecutive 1s are present.")
    return(str(k) + " consecutive 1s are NOT present.")
    
# Driver code
binary = 1111100000
k = 5
print(binaryCheck(binary,k))