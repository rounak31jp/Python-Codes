

Minimum cost to make all array elements equal
Given an array arr[] consisting of N positive integers, the task is to make all values of this array equal to some integer value 
with minimum cost after performing below operations any number of times (possibly zero).

Reduce the array element by 2 or increase it by 2 with zero cost.
Reduce the array element by 1 or increase it by 1 with a unit cost.
Examples:

Input: arr[] = {2, 4, 3, 1, 5}
Output: 2
We can change 3rd element to 5 incurring 0 cost.
We can change the 4th element to 5 ( 1 -> 3 -> 5 ) incurring 0 cost.
Now the array is, 2 4 5 5 5
We can change the 1st element to 5 (2 -> 4 -> 5 ) incurring unit cost.
We can change the 2nd element to 5 incurring unit cost.
Final array is, 5 5 5 5 5
Total cost = 1 + 1 = 2

Input: arr[] = {2, 2, 2, 3}
Output: 1
We can decrement last element by 1 incurring unit cost only.

Approach: The basic idea is to count the number of even elements and odd elements present in the array and print the 
minimum of these two as the answer. This approach works because we can make all even elements equal and all odd elements equal without incurring any cost 
(Operation 1). The updated array after performing these operations will only contain elements x and x + 1 where one is odd and the other 
is even. The elements from both the types can be changed into the other type with 1 unit cost and in order to minimise the cost, 
the result will be the min(frequency(x), frequency(x + 1)).





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
