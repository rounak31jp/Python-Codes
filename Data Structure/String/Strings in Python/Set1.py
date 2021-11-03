# Python code to demonstrate working of
# find() and rfind()
str = "geeksforgeeks is for geeks"
str2 = "geeks"

# using find() to find first occurrence of str2
# returns 8
print ("The first occurrence of str2 is at : ", end="")
print (str.find( str2, 4) )

# using rfind() to find last occurrence of str2
# returns 21
print ("The last occurrence of str2 is at : ", end="")
print ( str.rfind( str2, 4) )


==========================================================================================
==========================================================================================

# Python code to demonstrate working of
# startswith() and endswith()
str = "geeks"
str1 = "geeksforgeeksportal"

# using startswith() to find if str
# starts with str1
if str1.startswith(str):
		print ("str1 begins with : " + str)
else : print ("str1 does not begin with : "+ str)

# using endswith() to find
# if str ends with str1
if str1.endswith(str):
	print ("str1 ends with : " + str)
else :
	print ("str1 does not end with : " + str)



==========================================================================================
==========================================================================================


# Python code to demonstrate working of
# isupper() and islower()
str = "GeeksforGeeks"
str1 = "geeks"

# checking if all characters in str are upper cased
if str.isupper() :
	print ("All characters in str are upper cased")
else :
	print ("All characters in str are not upper cased")

# checking if all characters in str1 are lower cased
if str1.islower() :
	print ("All characters in str1 are lower cased")
else :
	print ("All characters in str1 are not lower cased")



==========================================================================================
==========================================================================================

# Python code to demonstrate working of
# upper(), lower(), swapcase() and title()
str = "GeeksForGeeks is fOr GeeKs"

# Converting string into its lower case
str1 = str.lower();
print (" The lower case converted string is : " + str1)

# Converting string into its upper case
str2 = str.upper();
print (" The upper case converted string is : " + str2)

# Converting string into its swapped case
str3 = str.swapcase();
print (" The swap case converted string is : " + str3)

# Converting string into its title case
str4 = str.title();
print (" The title case converted string is : " + str4)



==========================================================================================
==========================================================================================

# Python code to demonstrate working of
# len() and count()
str = "geeksforgeeks is for geeks"

# Printing length of string using len()
print (" The length of string is : ", len(str));

# Printing occurrence of "geeks" in string
# Prints 2 as it only checks till 15th element
print (" Number of appearance of ""geeks"" is : ",end="")
print (str.count("geeks",0,15))



==========================================================================================
==========================================================================================

# Python code to demonstrate working of
# center(), ljust() and rjust()
str = "geeksforgeeks"

# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(20,'-'))

# Printing the string after ljust()
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))

# Printing the string after rjust()
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))



==========================================================================================
==========================================================================================

# Python code to demonstrate working of
# isalpha(), isalnum(), isspace()
str = "geeksforgeeks"
str1 = "123"

# Checking if str has all alphabets
if (str.isalpha()):
	print ("All characters are alphabets in str")
else : print ("All characters are not alphabets in str")

# Checking if str1 has all numbers
if (str1.isalnum()):
	print ("All characters are numbers in str1")
else : print ("All characters are not numbers in str1")

# Checking if str1 has all spaces
if (str1.isspace()):
	print ("All characters are spaces in str1")
else : print ("All characters are not spaces in str1")




==========================================================================================
==========================================================================================
  
# Python code to demonstrate working of
# join()
str = "_"
str1 = ( "geeks", "for", "geeks" )

# using join() to join sequence str1 with str
print ("The string after joining is : ", end="")
print ( str.join(str1))

==========================================================================================
==========================================================================================
# Python code to demonstrate working of
# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"

# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )

# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )

# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )


==========================================================================================
==========================================================================================

# Python code to demonstrate working of
# min() and max()
str = "geeksforgeeks"

# using min() to print the smallest character
# prints 'e'
print ("The minimum value character is : " + min(str))

# using max() to print the largest character
# prints 's'
print ("The maximum value character is : " + max(str))

==========================================================================================
==========================================================================================

# Python code to demonstrate working of
# maketrans() and translate()
from string import maketrans # for maketrans()

str = "geeksforgeeks"

str1 = "gfo"
str2 = "abc"

# using maktrans() to map elements of str2 with str1
mapped = maketrans( str1, str2 )

# using translate() to translate using the mapping
print "The string after translation using mapped elements is : "
print str.translate(mapped)

==========================================================================================
==========================================================================================
# Python code to demonstrate working of
# replace()

str = "nerdsfornerds is for nerds"

str1 = "nerds"
str2 = "geeks"

# using replace() to replace str2 with str1 in str
# only changes 2 occurrences
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2))


==========================================================================================
==========================================================================================

# Python code to illustrate expandtabs()
string = 'GEEKS\tFOR\tGEEKS'

# No parameters, by default size is 8
print (string.expandtabs())

# tab size taken as 2
print(string.expandtabs(2))

# tab size taken as 5
print(string.expandtabs(5))

