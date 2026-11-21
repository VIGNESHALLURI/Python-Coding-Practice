#Write a program to create a tuple of five fruits and print all the elements.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits)

#Write a program to access individual elements from a given tuple using positive indexing and negative indexing.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits[0])
print(fruits[-1])

#Write a program to print all elements from a given tuple using positive indexing.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

#Write a program to print all elements from a given tuple using negative indexing.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])

#Write a program to access a group of elements from a given tuple using tuple slicing.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits[0:3])

#Write a program to find the total number of elements in a given tuple.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(len(fruits))

#Write a program to count the number of occurrences of a particular element in a given tuple.
fruits = ("Apple", "Banana", "Mango", "Apple", "Grapes")
print(fruits.count("Apple"))

#Write a program to find the index position of a particular element in a given tuple.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits.index("Mango"))

#Write a program to check whether a particular element is present in a given tuple.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print("Mango" in fruits)

#Write a program to concatenate two tuples and print all the elements.
fruits1 = ("Apple", "Banana", "Mango")
fruits2 = ("Orange", "Grapes")
fruits3 = fruits1 + fruits2
print(fruits3)