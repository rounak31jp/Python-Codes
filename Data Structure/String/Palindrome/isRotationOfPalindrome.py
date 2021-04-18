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




An Optimized Solution can work in O(n) time. 
The idea here is to use Manacher’s algorithm to solve the above problem.

Let the given string be ‘s’ and length of string be ‘n’.
Preprocess/Prepare the string to use Manachers Algorithm, to help find even length palindrome, for which 
we concatenate the given string with itself (to find if rotation will give a palindrome) and add ‘$’ symbol at 
the beginning and ‘#’ characters between letters. We end the string using ‘@’. 
So for ‘aaad’ input the reformed string will be – ‘$#a#a#a#a#d#a#a#a#a#d#@’
Now the problem reduces to finding Longest Palindromic Substring using Manacher’s algorithm of length n or greater in the string.
If there is palindromic substring of length n, then return true, else return false. If we find a palindrome of greater length then 
we check if the size of our input is even or odd, correspondingly our palindrome length found should also be even or odd.
For eg. if our input size is 3 and while performing Manacher’s Algorithm we get a palindrome size of 5 it obviously would 
contain a substring of size of 3 which is a palindrome but the same cannot be said for a palindrome of length of 4. 
Hence we check if both the size of the input and the size of palindrome found at any instance is both even or both odd.

Boundary case would be a word with same letters that would defy the above property but for that case our algorithm will find 
both even length and odd length palindrome one of them being a substring, hence it wont be a problem.

# Function to check if we have found
# a palindrome of same length as the input
# which is a rotation of the input string
def checkPal (x, Len):

	if (x == Len):
		return True
	elif (x > Len):
		if ((x % 2 == 0 and Len % 2 == 0) or (x % 2 != 0 and Len % 2 != 0)):
			return True

	return False

# Function to preprocess the string
# for Manacher's Algorithm
def reform (s):

	s1 = "$#"

	# Adding '#' between the characters
	for i in range(len(s)):
		s1 += s[i]
		s1 += "#"

	s1 += "@"
	return s1

# Function to find the longest palindromic
# substring using Manacher's Algorithm
def longestPal (s, Len):

	# Current Left Position
	mirror = 0
	
	# Center Right Position
	R = 0
	
	# Center Position
	C = 0
	
	# LPS Length Array
	P = [0] * len(s)
	x = 0
	
	# Get currentLeftPosition Mirror
	# for currentRightPosition i
	for i in range(1, len(s) - 1):
		mirror = 2 * C - i

		# If currentRightPosition i is
		# within centerRightPosition R
		if (i < R):
			P[i] = min((R-i), P[mirror])

		# Attempt to expand palindrome centered
		# at currentRightPosition i
		while (s[i + (1 + P[i])] == s[i - (1 + P[i])]):
			P[i] += 1

		# Check for palindrome
		ans = checkPal(P[i], Len)
		if (ans):
			return True
		
		# If palindrome centered at current
		# RightPosition i expand beyond
		# centerRightPosition R, adjust centerPosition
		# C based on expanded palindrome
		if (i + P[i] > R):
			C = i
			R = i + P[i]

	return False

# Driver Code
if __name__ == '__main__':
	
	s = "aaaad"
	Len = len(s)
	s += s
	s = reform(s)
	print(longestPal(s, Len))

