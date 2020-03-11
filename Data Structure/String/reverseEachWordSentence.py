# Python code to Reverse each word of a Sentence individually 
  
def reverseWordSentence(Sentence): 
  
    # Splitting the Sentence into list of words. 
    words = Sentence.split(" ") 
      
    # Reversing each word and creating a new list of words List Comprehension Technique 
    newWords = [word[::-1] for word in words] 
      
    # Joining the new list of words to for a new Sentence 
    newSentence = " ".join(newWords) 
  
    return newSentence 
  
Sentence = "Rounak Agarwal"
print(reverseWordSentence(Sentence))
