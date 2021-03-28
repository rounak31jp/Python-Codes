Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an array A: 
Example : 

Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
Output: 3 
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Input: A[] = {1, 2, 3} 
Output: -1 

--------------------------------------------------------------------------------------------------------------------------------------------

def equilibrium(arr):
    leftsum = 0
    rightsum = 0
    n = len(arr)
 
    for i in range(n):
        leftsum = 0
        rightsum = 0
     
        for j in range(i):
            leftsum += arr[j]
         
        for j in range(i + 1, n):
            rightsum += arr[j]
         
        if leftsum == rightsum:
            return i
     
    return -1
             
arr = [-7, 1, 5, 2, -4, 3, 0]
print (equilibrium(arr))



--------------------------------------------------------------------------------------------------------------------------------------------


def equilibrium(arr):
 
    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):
         
        total_sum -= num
         
        if leftsum == total_sum:
            return i
        leftsum += num

    return -1
     
# Driver code
arr = [-7, 1, 5, 2, -4, 3, 0]
print ('First equilibrium index is ',equilibrium(arr))
