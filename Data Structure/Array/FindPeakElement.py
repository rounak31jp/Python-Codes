# A python 3 program to find a peak element using divide and conquer 
  
def findPeakUtil(arr, low, high, n):  
    mid = low + (high - low)/2 
    mid = int(mid) 
      
    # Compare middle element with its neighbours (if neighbours exist) 
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and 
       (mid == n - 1 or arr[mid + 1] <= arr[mid])): 
        return mid 
  
  
    # If middle element is not peak and its left neighbour is greater  
    # than it, then left half must have a peak element 
    elif (mid > 0 and arr[mid - 1] > arr[mid]): 
        return findPeakUtil(arr, low, (mid - 1), n) 
  
    # If middle element is not peak and its right neighbour is greater 
    # than it, then right half must have a peak element 
    else: 
        return findPeakUtil(arr, (mid + 1), high, n) 
  
  
def findPeak(arr, n): 
    return findPeakUtil(arr, 0, n - 1, n) 
  
arr = [1, 3, 20, 4, 1, 0] 
n = len(arr) 
print("Index of a peak point is", findPeak(arr, n))
