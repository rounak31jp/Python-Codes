# Python3 program to show thatstring cannot be changed

a = 'Geeks'
print(a)
a[2] = 'E'
print(a) # causes error


==========================================================================================
==========================================================================================

# Python3 program to show that a string can be appended to a string.

a = 'Geeks'
print(a)
a = a + 'for'
print(a) # works fine


==========================================================================================
==========================================================================================

# Python3 program to show that both string hold same identity

string1 = "Hello"
string2 = "Hello"

print(id(string1))
print(id(string2))

==========================================================================================
==========================================================================================

# Modifying a string

string1 = "Hello"
print(id(string1))
string1 += "World"
print(string1)
print(id(string1))

==========================================================================================
==========================================================================================

# A python program to illustrate slicing in strings

x = "Geeks at work"
print (x[2])
print (x[6])
print (x[-3])
print (x[15])

==========================================================================================
==========================================================================================

# A python program to illustrate
# print substrings of a string
x = "Welcome to GeeksforGeeks"

# Prints substring from 2nd to 5th character
print (x[2:5])	

# Prints substring stepping up 2nd character
# from 4th to 10th character
print (x[4:10:2])	

# Prints 3rd character from rear from 3 to 5
print (x[-5:-3])	

==========================================================================================
==========================================================================================


