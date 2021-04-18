Given a string, Check if characters of the given string can be rearranged to form a palindrome. 

def canFormPalindrome(st):
    count = [0] * 256
    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1
    odd = 0  
    for i in range(0, NO_OF_CHARS):
        if (count[i] % 2 == 1):
            odd = odd + 1
        if (odd > 1):
            return False
    return True 
  
for _ in range(int(input())):
  str=input()
  print(canFormPalindrome(str))
