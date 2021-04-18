Given a string, the task is to find all the palindromic sub-strings from the given string.

def ispalindrome(str):
    first = 0
    last = len(str)-1
    
    while(first<=last):
        if(str[first]!=str[last]):
            return False
        first+=1
        last-=1
             
    return True

def allPalindromeSubstring(str):
    all_substrings=[]
    palindrome_subsstrings=[]
    
    for i in range(len(str)):
        for j in range(i,len(str)):
            all_substrings.append(str[i:j+1])
            
    for i in range(len(all_substrings)):
        if(ispalindrome(all_substrings[i])) :
            palindrome_subsstrings.append(all_substrings[i])
    
    print(palindrome_subsstrings)

for _ in range(int(input())):
    str=input()
    allPalindromeSubstring(str)
