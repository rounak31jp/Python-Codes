
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



