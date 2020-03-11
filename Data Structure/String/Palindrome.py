def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No")
    
    
    
    
 method 2
 
 def isPalindrome(s): 
      
    # Using predefined function to reverse to string print(s) 
    rev = ''.join(reversed(s)) 
    if (s == rev): 
        return True
    return False
   
s = "malayalam"
ans = isPalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No")
    
