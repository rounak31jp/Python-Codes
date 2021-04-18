Given two strings A and B of equal size. 
Two strings are equivalent either of the following conditions hold true:
1) They both are equal. Or,
2) If we divide the string A into two contiguous substrings of same size A1 and A2 and string B into two contiguous substrings 
of same size B1 and B2, then one of the following should be correct:
A1 is recursively equivalent to B1 and A2 is recursively equivalent to B2
A1 is recursively equivalent to B2 and A2 is recursively equivalent to B1
Check whether given strings are equivalent or not. Print YES or NO.





def recursive_equivalent(str_1,str_2):
    
    if(len(str_1)!=len(str_2)):
        return False
    
    char_list_1,char_list_2=[0]*256,[0]*256
    
    for i in range(len(str_1)):
        char_list_1[ord(str_1[i])]+=1
        char_list_2[ord(str_2[i])]+=1
        
    for k in range(256):
        if((char_list_1[k]-char_list_2[k])!=0):
            return False
        
    return True

def solution(a,b):
    if(a==b):
        return True
    a_1,a_2=a[0:len(a)//2],a[len(a)//2:len(a)]
    b_1,b_2=b[0:len(b)//2],b[len(b)//2:len(b)]
    
    if((recursive_equivalent(a_1,b_2) and recursive_equivalent(a_2,b_1)) or (recursive_equivalent(a_1,b_1) and recursive_equivalent(a_2,b_2))):
        return True
    
    return False
