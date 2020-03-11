K maximum sum combinations from two arrays
Given two equally sized arrays (A, B) and N (size of both arrays).
A sum combination is made by adding one element from array A and another element of array B. 
Display the maximum K valid sum combinations from all the possible sum combinations.

Examples:

Input :  A[] : {3, 2} 
         B[] : {1, 4}
         K : 2 [Number of maximum sum
               combinations to be printed]
Output : 7    // (A : 3) + (B : 4)
         6    // (A : 2) + (B : 4)

Input :  A[] : {4, 2, 5, 1}
         B[] : {8, 0, 3, 5}
         K : 3
Output : 13   // (A : 5) + (B : 8)
         12   // (A : 4) + (B :  8)
         10   // (A : 2) + (B : 8) 
         


import math  
from queue import PriorityQueue 
  
def KMaxCombinations( A, B, N, K): 
       
    pq = PriorityQueue()  
      
    for i in range(0, N): 
        for j in range(0, N): 
           a = A[i] + B[j]  
           pq.put((-a, a)) 
              
    count = 0
    while (count < K): 
        print(pq.get()[1]) 
        count = count + 1
          
A = [ 4, 2, 5, 1 ] 
B = [ 8, 0, 5, 3 ] 
N = len(A) 
K = 3
KMaxCombinations(A, B, N, K) 



