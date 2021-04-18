Check if a given string is a rotation of a palindrome
Given a string, check if it is a rotation of a palindrome. 
For example your function should return true for “aab” as it is a rotation of “aba”.

Examples:

Input:  str = "aaaad"
Output: 1  
// "aaaad" is a rotation of a palindrome "aadaa"
Input:  str = "abcd"
Output: 0
// "abcd" is not a rotation of any palindrome.

A Simple Solution is to take the input string, try every possible rotation of it and return true if a rotation is a palindrome. If no rotation is palindrome, then return false.
Following is the implementation of this approach.



# A utility function to check if a string str is palindrome
def isPalindrome(string):

	# Start from leftmost and rightmost corners of str
	l = 0
	h = len(string) - 1

	# Keep comparing characters while they are same
	while h > l:
		l+= 1
		h-= 1
		if string[l-1] != string[h + 1]:
			return False

	# If we reach here, then all characters were matching	
	return True

# Function to check if a given string is a rotation of a
# palindrome.
def isRotationOfPalindrome(string):

	# If string itself is palindrome
	if isPalindrome(string):
		return True

	# Now try all rotations one by one
	n = len(string)
	for i in xrange(n-1):
		string1 = string[i + 1:n]
		string2 = string[0:i + 1]

		# Check if this rotation is palindrome
		string1+=(string2)
		if isPalindrome(string1):
			return True

	return False

# Driver program
print "1" if isRotationOfPalindrome("aab") == True else "0"
print "1" if isRotationOfPalindrome("abcde") == True else "0"
print "1" if isRotationOfPalindrome("aaaad") == True else "0"

