## Python List/Array Methods
# 1.  Python List append() Method
# Add an element to the fruits list ...

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
#  sort()	Sorts the list

# Append  Add an element to the fruits list:
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)

#Clear  Remove all elements from the fruits list:
fruits1 = ["apple", "banana", "cherry"]
fruits1.clear()
print(fruits1)

#Copy  Copy the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

#count  Return the number of times the value "cherry" appears int the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

#Extend   Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#Index   What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# Insert : Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# POP Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#Remove  Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# Reverse   Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# Sort : Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)



######  Python Strings #######

# String Literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
print("Hello")
print('Hello')

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """Hello Raj , Ramana,
This is Practice tutorial,
String methods
This is Done."""
print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, Srinivas Kalyanapu!"
print(a[1])


# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
b = "Hello, Srinivas Kalyanapu!"
print(b[2:5])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Get the characters from position 5 to position 1, starting the count from the end of the string:
b = "Hello, Srinivas Kalyanapu!"
print(b[-5:-2])

# String Length
# To get the length of a string, use the len() function.
# The len() function returns the length of a string:

a = "Hello, Srinivas!"
print(len(a))

# strip() method 
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello,World! "
print(a.strip())




