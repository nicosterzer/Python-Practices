# Introduction to the program.
print("Welcome to the Average Score Calculator!")
print("Insert the score in each subject, from 1-10")
print(" ") 

# Number of different subjects to calculate the average score from.
Science = int(input("Science: "))
Maths = int(input("Maths: "))
SS = int(input("Social Studies: "))
English = int(input("English: "))
Spanish = int(input("Spanish: "))

# Sums the input of all of the subjects and divides it between the total amount of subjects.
sum = Science + Maths + SS + English + Spanish
result = int(sum // 5)

# Conditional statement which determines whether the student passed or not.
if result >= 6:

  print("Student passed")

elif result <= 5:
  
  print("Student failed")

print("Software created by Nicolás Sterzer")