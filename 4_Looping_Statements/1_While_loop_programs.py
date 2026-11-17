# 1. Print numbers from 1 to 10.
num = 1
while num <= 10:
    print(num)
    num = num + 1

# 2. Print numbers from 10 to 1.
num = 10
while num >= 1:
    print(num)
    num = num - 1

# 3. Print even numbers from 1 to 50.
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num)
    num = num + 1

# 4. Print odd numbers from 1 to 50.
num = 1
while num <= 50:
    if num % 2 != 0:
        print(num)
    num = num + 1

# 5. Find the sum of numbers from 1 to 10.
num = 1
total = 0
while num <= 10:
    total = total + num
    num = num + 1
print("Total sum:", total)

# 6. Print the multiplication table of a number.
num = 5
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1

# 7. Count the digits in a number.
num = 12345
count = 0
while num > 0:
    count = count + 1
    num = num // 10

print("Total digits:", count)

# 8. Find the factorial of a number.
num = 5
i = 1
fact = 1
while i <= num:
    fact = fact * i
    i = i + 1

print("Factorial:", fact)

# 9. Reverse a given number.
num = 12345
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse number:", reverse)

# 10. Check whether a number is a palindrome.
num = 121
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

