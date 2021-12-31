'''
String slicing in Python to check if a string can become empty by recursive deletion
Given a string “str” and another string “sub_str”. We are allowed to delete “sub_str” from “str” any number of times. It is also given that the “sub_str” appears only once at a time. The task is to find if “str” can become empty by removing “sub_str” again and again.

Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
Output : Yes
Explanation : In the string GEEGEEKSKS, we can first 
              delete the substring GEEKS from position 4.
              The new string now becomes GEEKS. We can 
              again delete sub-string GEEKS from position 1. 
              Now the string becomes empty.


Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
Output : No
Explanation : In the string it is not possible to make the
              string empty in any possible manner.
'''

def checkEmpty(Input,pattern):
    if len(Input) == 0 and len(pattern) == 0:
        return True
    if len(pattern) == 0:
        return True
    while (len(Input)) != 0:
        index = Input.find(pattern) 
        if index == -1:
            return False
        Input = Input[0:index] + Input[index + len(pattern):]
    return True
    
# Driver program 
if __name__ == "__main__": 
    Input ='GEEGEEKSKS'
    pattern =''
    print (checkEmpty(Input, pattern))
