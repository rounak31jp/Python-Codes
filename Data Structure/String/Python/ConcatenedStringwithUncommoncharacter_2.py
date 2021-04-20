Concatenated string with uncommon characters of two strings
Difficulty Level : Medium
Two strings are given and you have to modify 1st string such that all the common characters of the 2nd strings have to be removed 
and the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.

Examples:

Input : S1 = "aacdb"
        S2 = "gafd"
Output : "cbgf"

Input : S1 = "abcs";
        S2 = "cxzca";
Output : "bsxz"



def solution(s1,s2):
    res=""
    m = {}
    
    for i in range(len(s2)):
        m[s2[i]] = 1
        
    for i in range(len(s1)):
        if(s1[i] not in m):
            res+=s1[i]
        else:
            m[s1[i]]= 2
            
    for i in range(len(s2)):
        if(m[s2[i]]==1):
            res+=s2[i]

    print(res)
