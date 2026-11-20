#Write a program to create a list of five bikes and print all the elements.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
print(bikes)

#Write a program to access individual elements from a given list using positive indexing and negative indexing.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
print(bikes[0])
print(bikes[-1])

#Write a program to print all elements from a given list using positive indexing.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
print(bikes[0])
print(bikes[1])
print(bikes[2])
print(bikes[3])
print(bikes[4])

#Write a program to print all elements from a given list using negative indexing.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
print(bikes[-1])
print(bikes[-2])
print(bikes[-3])
print(bikes[-4])
print(bikes[-5])

#Write a program to access a group of elements from a given list using list slicing.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
print(bikes[0:3])

#Write a program to find the total number of elements in a given list.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
print(len(bikes))

#Write a program to add a new element to the end of a given list.
bikes = ["Yamaha", "Unicorn", "Duke"]
bikes.append("Royal Enfield")
print(bikes)

#Write a program to insert an element at a specific position in a given list.
bikes = ["Yamaha", "Royal Enfield", "Pulsar", "Duke"]
bikes.insert(1, "Unicorn")
print(bikes)

#Write a program to remove a particular element from a given list.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
bikes.remove("Pulsar")
print(bikes)

#Write a program to reverse the elements of a given list.
bikes = ["Yamaha", "Royal Enfield", "Unicorn", "Pulsar", "Duke"]
bikes.reverse()
print(bikes)
