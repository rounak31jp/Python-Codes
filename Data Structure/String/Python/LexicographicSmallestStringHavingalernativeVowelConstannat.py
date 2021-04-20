Alternate vowel and consonant string
Difficulty Level : Medium
Last Updated : 14 Jun, 2019
Given a string, rearrange characters of the given string such that the vowels and consonants occupy alternate position. 
If string can not be rearranged in desired way, print “no such string”. 
The order of vowels with respect to each other and the order of consonants with respect to each other should be maintained.

If more than one required strings can be formed, print the lexicographically smaller.

Examples:

Input : geeks
Output : gekes

Input : onse
Output : nose
There are two possible outcomes
"nose" and "ones".  Since "nose"
is lexicographically smaller, we 
print it.



def isvowel(s):
    if s in "aeiouAEIOU":
        return True
    return False
      
def solution(s1):
    count,vowel_count,consnt_count=len(s1),0,0
    itr,diff=0,0
    vowel_str,consnt_str,answer="","",""
    for i in range(count):
        if(isvowel(s1[i])):
            vowel_count+=1
            vowel_str+=s1[i]
        else:
            consnt_str+=s1[i]
    consnt_count=count-vowel_count
    
    if(vowel_count-consnt_count>1 or consnt_count-vowel_count>1):
        print("No Such String")
        
    if(vowel_count>consnt_count):
        itr=min(vowel_count,consnt_count)
        for i in range(itr):
            answer=answer+vowel_str[i]+consnt_str[i]
        answer+=vowel_str[itr]
        
    if(consnt_count>vowel_count):
        itr=min(vowel_count,consnt_count)
        for i in range(itr):
            answer=answer+consnt_str[i]+vowel_str[i]
        answer+=consnt_str[itr]
    
    if(consnt_count==vowel_count):
        itr=min(vowel_count,consnt_count)
        if(ord(vowel_str[0])>ord(consnt_str[0])):
            for i in range(itr):
                answer=answer+consnt_str[i]+vowel_str[i]
        else:
            for i in range(itr):
                answer=answer+vowel_str[i]+consnt_str[i]

    print(answer)
