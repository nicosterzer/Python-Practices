print("Welcome to the Average Score Calculator!")
print("Insert the score in each subject, from 1-10")
print(" ") 

Science = int(input("Science: "))
Maths = int(input("Maths: "))
SS = int(input("Social Studies: "))
English = int(input("English: "))
Spanish = int(input("Spanish: "))

sum = Science + Maths + SS + English + Spanish
result = int(sum // 5)

if result >= 6:
  print("Student passed")
elif result <= 5:
  print("Student failed")

print("Software created by Nicolás Sterzer")