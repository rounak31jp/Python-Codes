Given two strings X and Y of length N, the task is to check if both the strings can be made equal by reversing any substring of X exactly once. 
If it is possible, then print “Yes”. Otherwise, print “No”.

Examples:
Input: X = “adcbef”, Y = “abcdef”
Output: Yes
Explanation: Strings can be made equal by reversing the substring “dcb” of string X.
Input: X = “126543”, Y = “123456”
Output: Yes
Explanation: Strings can be made equal by reversing the substring “6543” of string X.

  
  

def TwoStringMadeEqualByRotatingSubsstring(a,b):
    
    if(len(a)!=len(b)):
        return False
    
    right,left=0,len(a)-1
    
    while(right<=len(a) and a[right]==b[right]):
        right=right+1
    while(left>=0 and a[left]==b[left]):
        left=left-1
    
    a_1=a[right:left+1]
    b_1=b[right:left+1]
    
    if(a_1[::-1]==b_1 or b_1[::-1]==a_1):
        return True
    
    return False
  
  TwoStringMadeEqualByRotatingSubsstring("126543","123456")
