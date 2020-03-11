

Move all negative elements to end in order with extra space allowed
Given an unsorted array of both negative and positive integer. 
The task is place all negative element at the end of array without changing the order of positive element and negative element.






def segregateElements(arr, n): 
    temp = [0 for k in range(n)] 
    j = 0  
    for i in range(n): 
        if (arr[i] >= 0 ): 
            temp[j] = arr[i] 
            j +=1
   
    if (j == n or j == 0): 
        return
   
    for i in range(n): 
        if (arr[i] < 0): 
            temp[j] = arr[i] 
            j +=1
   
    for k in range(n): 
        arr[k] = temp[k] 
  
arr = [1 ,-1 ,-3 , -2, 7, 5, 11, 6 ] 
n = len(arr) 
  
segregateElements(arr, n); 
   
for i in range(n): 
    print (arr[i],end=" ")

    
