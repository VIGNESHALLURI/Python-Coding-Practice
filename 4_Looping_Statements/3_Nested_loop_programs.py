# 1. Write a Python program to print a 5x5 square star pattern.
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# 2. Write a Python program to print a right-angle triangle star pattern.
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 3. Write a Python program to print an inverted right-angle triangle star pattern.
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 4. Write a Python program to print a square pattern using numbers.
for i in range(1, 5):
    for j in range(1, 5):
        print(j, end=" ")
    print()

# 5. Write a Python program to print the same number in each row.
for i in range(1, 6):
    for j in range(5):
        print(i, end=" ")
    print()

# 6. Write a Python program to print a number triangle pattern.
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 7. Write a Python program to print an inverted number triangle pattern.
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 8. Write a Python program to print multiplication tables from 1 to 5.
for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

# 9. Write a Python program to print all pairs of numbers from 1 to 3.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# 10. Write a Python program to print a 5x5 pattern using alternating 1s and 0s.
for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
