String with k distinct characters and no same characters adjacent
Difficulty Level : Easy
Given N and K, print a string that has n characters. 
The string should have exactly k distinct characters and no adjacent positions.

Examples:

Input  : n = 5, k = 3 
Output :  abcab
Explanation: 3 distinct character a, b, c
and n length string. 

Input: 3 2
Output: aba 
Explanation: 2 distinct character 'a' 
and 'b' and n length string.



def solution(n,k):
    ans=""
    divisor=n//k
    remainder=n%k
    for i in range(k):
        ans+=chr(ord('a')+i)
    ans=ans*divisor
    for i in range(remainder):
        ans+=chr(ord('a')+i) 
    print(ans)
