Check if a given string is a rotation of a palindrome
Given a string, check if it is a rotation of a palindrome. 
For example your function should return true for “aab” as it is a rotation of “aba”.

Examples:

Input:  str = "aaaad"
Output: 1  
// "aaaad" is a rotation of a palindrome "aadaa"

Input:  str = "abcd"
Output: 0
// "abcd" is not a rotation of any palindrome.



def ispalindrome(str):
    first = 0
    last = len(str)-1
    
    while(first<=last):
        first+=1
        last-=1
        if(str[first]!=str[last]):
            return False
        
    return True

def rotationispalindrome(str):
    n=len(str)
    for i in range(n):
        new_str=str[i+1:n]+str[0:i+1]
        if ispalindrome(new_str):
            return True
    return False

for _ in range(int(input())):
    str=input()
    print(rotationispalindrome(str))
