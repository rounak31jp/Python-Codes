#An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. 
#For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2


def printLeaders(arr,size): 
      
    for i in range(0, size): 
        for j in range(i+1, size): 
            if arr[i]<arr[j]: 
                break
        if j == size-1:
            print (arr[i]), 
   
arr = [16, 17, 4, 3, 5, 2] 
printLeaders(arr, len(arr))
