# Student Information Script
# Made by: Amad Bin Jaiyad

# Taking inputs
name = input("Enter your name: ")              # string
age = int(input("Enter your age: "))           # int
course = input("Enter your course: ")          # string
college = input("Enter your college name: ")   # string
marks = float(input("Enter your marks: "))     # float
is_passed = marks >= 40                        # boolean

# Printing details
print("\n----- Student Information -----")
print("Name: ", name)
print("Age: ", age)
print("Course: ", course)
print("College: ", college)
print("Marks: ", marks)
print("Passed: ", is_passed)   # True if marks >= 40, False otherwise
