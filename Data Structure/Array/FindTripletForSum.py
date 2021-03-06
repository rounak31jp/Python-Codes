# Python3 program to find a triplet that sum to a given value 
  
# returns true if there is triplet with sum equal to 'sum' present in A[].  
# Also, prints the triplet 

def find3Numbers(A, arr_size, sum): 
    for i in range( 0, arr_size-2): 
        for j in range(i + 1, arr_size-1):  
            for k in range(j + 1, arr_size): 
                if A[i] + A[j] + A[k] == sum: 
                    print("Triplet is",A[i],",",A[j],",",A[k]) 
                    return True
    return False
   
A = [1, 4, 45, 6, 10, 8] 
sum = 22
arr_size = len(A) 
find3Numbers(A, arr_size, sum)




Method 2


def find3Numbers(A, arr_size, sum): 
  
    # Sort the elements  
    A.sort() 
  
    # Now fix the first element one by one and find the other two elements  
    for i in range(0, arr_size-2): 
      
  
        # To find the other two elements start two index variables from 
        # two corners of the array and move them toward each other 
        l = i + 1 
        r = arr_size-1 
        while (l < r): 
          
            if( A[i] + A[l] + A[r] == sum): 
                print("Triplet is", A[i],', ', A[l], ', ', A[r]); 
                return True
              
            elif (A[i] + A[l] + A[r] < sum): 
                l += 1
            else: # A[i] + A[l] + A[r] > sum 
                r -= 1
    return False
    
A = [1, 4, 45, 6, 10, 8] 
sum = 22
arr_size = len(A) 
  
find3Numbers(A, arr_size, sum)





Method 3

def find3Numbers(A, arr_size, sum): 
    for i in range(0, arr_size-1): 
        # Find pair in subarray A[i + 1..n-1] with sum equal to sum - A[i] 
        s = set() 
        curr_sum = sum - A[i] 
        for j in range(i + 1, arr_size): 
            if (curr_sum - A[j]) in s: 
                print("Triplet is", A[i],", ", A[j], ", ", curr_sum-A[j]) 
                return True
            s.add(A[j]) 
      
    return False
  
# Driver program to test above function  
A = [1, 4, 45, 6, 10, 8]  
sum = 22
arr_size = len(A)  
find3Numbers(A, arr_size, sum)
