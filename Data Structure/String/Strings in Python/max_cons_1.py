Maximum length of consecutive 1’s in a binary string in Python using Map function

We are given a binary string containing 1’s and 0’s. Find the maximum length of consecutive 1’s in it.
Input : str = '11000111101010111'
Output : 4
  
# Function to find Maximum length of consecutive 1's in a binary string

def maxConsecutive1(input):
	# input.split('0') --> splits all sub-strings of consecutive 1's
	# separated by 0's, output will be like ['11','1111','1','1','111']
	# map(len,input.split('0')) --> map function maps len function on each
	# sub-string of consecutive 1's
	# max() returns maximum element from a list
	print max(map(len,input.split('0')))

# Driver program
if __name__ == "__main__":
	input = '11000111101010111'
	maxConsecutive1(input)

  
  
