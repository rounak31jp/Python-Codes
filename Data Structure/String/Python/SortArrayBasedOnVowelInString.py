Given an array arr[] of N strings, the task is to sort these strings according to the numbers of vowels in them

def is_vowel(ch):
    if ch in "AEIOUaeiou":
        return True
    return False

def vowel_count(str):
    vowel_count=0
    for i in range(len(str)):
        if(is_vowel(str[i])):
            vowel_count+=1 
    return vowel_count    

def SortArrayBasedOnVowelInString(arr):
    vec=[]
    for i in range(len(arr)):
        vec.append((vowel_count(arr[i]),arr[i]))
    vec.sort()
    
    print(vec)
    
    for i in range(len(vec)):
        print(vec[i][1],end=" ")
        
SortArrayBasedOnVowelInString([ "lmno", "pqrst","aeiou", "xyz" ])
