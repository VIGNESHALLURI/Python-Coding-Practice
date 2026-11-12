#Demonstrate logical AND.
a = 10
b = 20
print(a > 5 and b > 15)

#Demonstrate logical OR.
a = 10
b = 5
print(a > 15 or b < 10)

#Demonstrate logical NOT.
a = True
print(not a)

#Check whether a number is between 1 and 100.
num = 40
print(num >= 1 and num <= 100)

#Check voting eligibility using age and citizenship.
age = 23
citizen = True
print(age >= 18 and citizen == True)

#Check whether a student passed two subjects.
maths = 75
science = 65
print(maths >= 35 and science >= 35)

#Check loan eligibility using age and salary.
age = 25
salary = 50000
print(age >= 21 and salary >= 30000)

#Check divisibility by both 5 and 10.
num = 50
print(num % 5 == 0 and num % 10 == 0)

#Check whether a number is outside the range 10–50.
num = 60
print(num < 10 or num > 50)

#Check login conditions using username and password.
username = "admin"
password = "12345"
print(username == "admin" and password == "12345")