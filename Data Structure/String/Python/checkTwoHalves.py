Given a string of lowercase characters only, the task is to check if it is possible to split a string from middle which will gives two halves 
having the same characters and same frequency of each character.

def solution(str):
    
    length_by_2=int(len(str)//2)
    
    if(len(str)%2!=0):
        return False
    
    str1,str2=str[0:length_by_2],str[length_by_2:n]
    
    char_list_1,char_list_2=[0]*256,[0]*256
    
    for i in range(length_by_2):
        char_list_1[ord(str1[i])]+=1
        char_list_2[ord(str2[i])]+=1
        
    for k in range(256):
        if((char_list_1[k]-char_list_2[k])!=0):
            return False
        
    return True
