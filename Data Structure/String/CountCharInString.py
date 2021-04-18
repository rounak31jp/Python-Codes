def CountCharInString(str):
    a=[0]*256
    for i in range(len(str)):
        a[ord(str[i])]+=1
    
    for i in range(len(a)):
        if(a[i]!=0):
            print(chr(i),a[i])
