#Write a Python program to print numbers from 1 to 100 that are divisible by 5.
for num in range(1, 101):
    if num % 5 == 0:
        print(num)

#Write a Python program to find the sum of all odd numbers from 1 to 50.
total = 0
for num in range(1, 51):
    if num % 2 != 0:
        total = total + num
print("Sum of odd numbers:", total)

#Write a Python program to find the sum of all even numbers from 1 to 100.
total = 0
for num in range(1, 101):
    if num % 2 == 0:
        total = total + num
print("Sum of even numbers:", total)

#Write a Python program to print the squares of numbers from 1 to 10.
for num in range(1, 11):
    print(num, "square is", num * num)

#Write a Python program to print the cubes of numbers from 1 to 10.
for num in range(1, 11):
    print(num, "cube is", num * num * num)

#Write a Python program to find the largest number in a list.
numbers = [12, 45, 23, 67, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)

#Write a Python program to find the smallest number in a list.
numbers = [25, 10, 45, 5, 30]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)

#Write a Python program to count how many positive numbers are in a list.
numbers = [10, -5, 20, -8, 15, 0]
count = 0
for num in numbers:
    if num > 0:
        count = count + 1
print("Positive numbers count:", count)

#Write a Python program to print each character of a given string.
name = "vignesh"
for char in name:
    print(char)

#Write a Python program to calculate the total marks of five subjects.
marks = [85, 90, 78, 88, 92]
total = 0
for mark in marks:
    total = total + mark
print("Total marks:", total)

