from collections import Counter
def lambdafilterexample(my_list,str1):
#    a = list(filter(lambda x: (x%13 == 0), my_list)) -- return list of no. divisible by 13 - input my_list
#    a = list(filter(lambda x : (x == "".join(reversed(x))),my_list)) -- return palandrome - input my_list
    a = list(filter(lambda x : (Counter(x) == Counter(str1)),my_list)) # return anagram of str1 from my_list - input my_list, str1
    return a
# Driver code
# my_list = [12, 65, 54, 39, 102,339, 221, 50, 70] 
# my_list = ["geeks", "geeg", "keek", "practice", "aa"]
my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str1 = "eegsk"
print(lambdafilterexample(my_list,str1))