def minCost(arr, n): 

    count_even = 0
    count_odd = 0

    for i in range(n): 
        if (arr[i] % 2 == 0): 
            count_even += 1
        else: 
            count_odd += 1
  
    return min(count_even, count_odd) 
  
arr = [2, 4, 3, 1, 5] 
n = len(arr) 
  
print(minCost(arr, n)) 
