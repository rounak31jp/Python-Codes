Given a string, find the longest substring which is palindrome

def ispalindrome(str):
    first = 0
    last = len(str)-1
    
    while(first<=last):
        if(str[first]!=str[last]):
            return False
        first+=1
        last-=1
             
    return True

def longestPalSubstr(str):
    all_substrings=[]
    palindrome_subsstrings=[]
    
    for i in range(len(str)):
        for j in range(i,len(str)):
            all_substrings.append(str[i:j+1])
            
    for i in range(len(all_substrings)):
        if(ispalindrome(all_substrings[i])) :
            palindrome_subsstrings.append(all_substrings[i])
           
    print("longest palindrome string in",str,"is",max(palindrome_subsstrings, key = len),"with length",len(max(palindrome_subsstrings, key = len)))
    
for _ in range(int(input())):
    str=input()
    longestPalSubstr(str)
