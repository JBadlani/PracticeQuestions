'''
Concatenated string with uncommon characters in Python
Input : S1 = "aacdb"
        S2 = "gafd"
Output : "cbgf"

Input : S1 = "abcs";
        S2 = "cxzca";
Output : "bsxz"
'''

def uncommonConcat(s1,s2):
    s1 = set(s1) #acdb
    s2 = set(s2) #gafd
    common = list(s1&s2) #[a,d]
    result = [c for c in s1 if c not in common] + [c for c in s2 if c not in common]
    return ''.join(result)
        
s1 = "aacdb"
s2 = "gafd"
print(uncommonConcat(s1,s2))