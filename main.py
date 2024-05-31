# Name: Chike-Mozie Charles Chukwuemeka
# Student ID: IDEAS/24/88679
# Email: Charleschukwuemeka47@gmail.com

name = "Chike-Mozie Charles Chukwuemeka"
studentId = "IDEAS/24/88679"
email = "Charleschukwuemeka47@gmail.com"

# Exercises and Lessons
# Exercise: Insert the missing part of the code below to output "Hello World".
print("Hello World")

# Global variables, usage and how to change them
new_language = "Go lang" #new_language is a global variable

# Define a new function
def myfunc():
  global new_language
  new_language = "python"
  print("I changed the global variable from Go lang to" , new_language)

myfunc()

# Variable Exercises
# 1. Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"

# 2. Create a variable named x and assign the value 50 to it.
x = 50

# 3. Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(x + y)

# 4. Create a variable called z, assign x + y to it, and display the result.
x = 5
y = 10
z = x + y
print(z)

# 5. Insert the correct syntax to assign values to multiple variables in one line:
x , y , z = "Orange", "Banana", "Cherry"

# 6. Insert the correct syntax to assign the same value to all three variables in one code line
x = y = z = "Orange"

# 7.Insert the correct keyword to make the variable x belong to the global scope.

def myfunc():
  global x
  x = "fantastic"
  
# Different Data Types
string = "Hello"
integer = 2
floating_number = 35.3
complex_number = 3j
a_list = ["apple", "food", "mango"]
a_tuple = ("apple", "food", "mango")
a_range = range(6)


print(type(string))
print(type(integer))
print(type(floating_number))
print(type(complex_number))
print(type(a_list))
print(type(a_tuple ))
print(type(a_range ))

submission = f"This assignment was submitted by: {name} that has a Student ID of: {studentId}, and the email of: {email}"
print(submission)
