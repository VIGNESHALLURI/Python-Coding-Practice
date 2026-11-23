# 1. Write a Python program to create a set of student names and print all set elements.
set1 = {"rajesh", "suresh", "vignesh", "manish"}
print(set1)

# 2. Write a Python program to find the length of a set containing duplicate elements.
numbers = {10, 20, 20, 40, 59, 40, 67, 89, 67}
print("Set elements:", numbers)
print("Length of set:", len(numbers))

# 3. Write a Python program to convert a string into a set and print the result.
state = "Andhra Pradesh"
result = set(state)
print(result)

# 4. Write a Python program to convert a list of student names into a set and remove duplicate names.
my_friends = ["Karthik", "rajesh", "surya", "praveen", "manish"]
result = set(my_friends)
print(result)

# 5. Write a Python program to create a set containing both homogeneous and heterogeneous elements.
my_set = {10, 20, 30, "python", "java", 45.5, True}
print(my_set)

# 6. Write a Python program to add a new student name to an existing set.
students = {"rajesh", "suresh", "vignesh"}
students.add("manish")
print(students)

# 7. Write a Python program to add multiple elements to a set using update().
numbers = {10, 20, 30}
numbers.update([40, 50, 60])
print(numbers)

# 8. Write a Python program to remove duplicate numbers from a list using a set.
numbers = [10, 20, 30, 10, 40, 20, 50, 30, 60]
unique_numbers = set(numbers)
print(unique_numbers)

# 9. Write a Python program to check whether a set is mutable by adding and removing elements.
numbers = {10, 20, 30, 40}
numbers.add(50)
numbers.remove(20)
print(numbers)

# 10. Write a Python program to check whether a set allows duplicate elements.
numbers = {10, 20, 30, 10, 20, 40, 50, 30}
print("Set elements:", numbers)
print("Number of unique elements:", len(numbers))