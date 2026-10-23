# Python Fundamentals: Sample Data
# Topics: Variables, Data Types, Input, Counting, and Slicing

# 1. Variables and input
student_name = input("Enter your name: \n")
age = int(input("Enter your age: \n"))
favorite_language = input("Enter your favorite programming language: \n")

# 2. Display student information
print("\nSTUDENT INFORMATION")
print("Name:", student_name)
print("Age:", age)
print("Favorite language:", favorite_language)

# 3. Data types
print("\nDATA TYPES")
print("Name type:", type(student_name))
print("Age type:", type(age))
print("Favorite language type:", type(favorite_language))

# 4. Counting characters
print("\nCOUNTING")
print("Number of characters in your name:", len(student_name))

# 5. Slicing strings
print("\nSLICING")
print("First two characters of your name:", student_name[:2])
print("First three characters of your favorite language:", favorite_language[:3])
