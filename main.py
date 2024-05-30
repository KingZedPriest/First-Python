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

print("This assignment was submitted by:", name, "that has a Student ID of:", studentId, "and the email of:", email)
