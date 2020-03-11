# Python code to print Second most repeated word in a sequence in Python 
from collections import Counter 
  
def secondFrequent(input): 
  
    # Convert given list into dictionary 
    # it's output will be like {'ccc':1,'aaa':3,'bbb':2} 
    dict = Counter(input) 
  
    # Get the list of all values and sort it in ascending order 
    value = sorted(dict.values(), reverse=True) 
  
    # Pick second largest element 
    secondLarge = value[1] 
  
    # Traverse dictionary and print key whose 
    # value is equal to second large element 
    for (key, val) in dict.items(): 
        if val == secondLarge: 
            print (key) 
            return
  
if __name__ == "__main__": 
    input = ['aaa','bbb','ccc','bbb','aaa','aaa'] 
    secondFrequent(input)
