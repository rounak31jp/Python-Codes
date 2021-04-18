Given a string, Check if characters of the given string can be rearranged to form a palindrome. 
For example characters of “geeksogeeks” can be rearranged to form a palindrome “geeksoskeeg”, 
but characters of “geeksforgeeks” cannot be rearranged to form a palindrome.

A set of characters can form a palindrome if at most one character occurs odd number of times and all characters occur even number of times.
A simple solution is to run two loops, the outer loop picks all characters one by one, the inner loop counts the number of occurrences of the picked character. 
We keep track of odd counts. Time complexity of this solution is O(n2).
We can do it in O(n) time using a count array. Following are detailed steps. 
Create a count array of alphabet size which is typically 256. Initialize all values of count array as 0.
Traverse the given string and increment count of every character.
Traverse the count array and if the count array has more than one odd values, return false. Otherwise, return true.


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
