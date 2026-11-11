#Convert an integer into a float.
num = 25
result = float(num)
print(result)
print(type(result))

#Convert a float into an integer.
num = 25.75
result = int(num)
print(result)
print(type(result))

#Convert an integer into a string.
num = 100
result = str(num)
print(result)
print(type(result))

#Convert a numeric string into an integer.
num = "250"
result = int(num)
print(result)
print(type(result))

#Convert a numeric string into a float.
num = "45.75"
result = float(num)
print(result)
print(type(result))

#Convert an integer into a Boolean.
num = 10
result = bool(num)
print(result)
print(type(result))

#Convert a Boolean into an integer.
value = True
result = int(value)
print(result)
print(type(result))

#Convert a float into a string.
num = 34.66
result = str(num)
print(result)
print(type(result))

#Take two numbers as input, convert them into integers and calculate their sum.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = int(num1) + int(num2)
print("Sum:", result)

#Take salary as a string, convert it into a float and calculate annual salary.
salary = input("Enter your monthly salary: ")

monthly_salary = float(salary)
annual_salary = monthly_salary * 12

print("Monthly Salary:", monthly_salary)
print("Annual Salary:", annual_salary)