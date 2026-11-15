# Write a Python program to check whether a given number is a single-digit, two-digit, three-digit, or more-than-three-digit number.
num = 456
if num <= 9:
    print("Single digit")
elif num <= 99:
    print("Two digit")
elif num <= 999:
    print("Three digit")
else:
    print("More than three digits")

#Write a Python program to calculate the movie ticket price based on a person's age.
age = 25
if age < 12:
    print("Ticket price: Rs.100")
elif age <= 18:
    print("Ticket price: Rs.150")
elif age <= 60:
    print("Ticket price: Rs.200")
else:
    print("Ticket price: Rs.120")

#Write a Python program to display a student's grade based on marks (Excellent, Very Good, Good, Pass, or Fail).
marks = 85
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 50:
    print("Good")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

#Write a Python program to find the largest number among three given numbers.
a = 45
b = 78
c = 32
if a > b and a > c:
    print("A is largest")
elif b > a and b > c:
    print("B is largest")
else:
    print("C is largest")

#Write a Python program to classify internet speed as Slow, Average, Good, or Excellent.
speed = 45
if speed < 10:
    print("Slow")
elif speed <= 30:
    print("Average")
elif speed <= 60:
    print("Good")
else:
    print("Excellent")

#Write a Python program to calculate the discount based on the total shopping amount.
amount = 6000
if amount >= 10000:
    discount = amount * 0.25
elif amount >= 5000:
    discount = amount * 0.15
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0
print("Discount:", discount)
print("Final amount:", amount - discount)

#Write a Python program to check whether a given character is uppercase, lowercase, a digit, or a special character.
char = "A"
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")

#Write a Python program to check whether a person is eligible for a learner licence or regular driving licence based on age.
age = 20
if age < 16:
    print("Not eligible")
elif age < 18:
    print("Learner licence category")
else:
    print("Regular licence category")

#Write a Python program to calculate an employee's bonus based on years of experience.
experience = 6
if experience >= 10:
    print("20% bonus")
elif experience >= 5:
    print("15% bonus")
elif experience >= 2:
    print("10% bonus")
else:
    print("No bonus")

#Write a Python program to display the water tank status as Empty, Low, Medium, High, or Full based on the water percentage.
level = 60
if level == 0:
    print("Empty")
elif level <= 25:
    print("Low")
elif level <= 50:
    print("Medium")
elif level <= 75:
    print("High")
elif level <= 100:
    print("Full")
else:
    print("Invalid level")