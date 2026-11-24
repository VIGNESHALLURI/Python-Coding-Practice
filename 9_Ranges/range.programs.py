#Write a Python program to print numbers from 0 to 6 using range().
for num in range(7):
    print(num)

#Write a Python program to print numbers from 3 to 11 using range().
for num in range(3, 12):
    print(num)

#Write a Python program to print even numbers from 0 to 14 using range().
for num in range(0, 15, 2):
    print(num)

#Write a Python program to print odd numbers from 1 to 19 using range().
for num in range(1, 20, 2):
    print(num)

#Write a Python program to print numbers from 10 to 1 in reverse order.
for num in range(10, 0, -1):
    print(num)

#Write a Python program to print multiples of 5 from 5 to 50.
for num in range(5, 51, 5):
    print(num)

#Write a Python program to calculate the sum of numbers from 1 to 10.
total = 0
for num in range(1, 11):
    total += num
print("Total:", total)

#Write a Python program to print the multiplication table of a number.
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#Write a Python program to print numbers from -5 to 15 with a step size of 3.
for num in range(-5, 16, 3):
    print(num)

#Write a Python program to count numbers divisible by 3 between 1 and 30.
count = 0
for num in range(1, 31):
    if num % 3 == 0:
        count += 1
print("Count:", count)