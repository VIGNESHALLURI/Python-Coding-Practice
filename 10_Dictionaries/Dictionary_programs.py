#Create a dictionary with student details and print it.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python"
}
print(student)

#Access the student's name and age from the dictionary.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python"
}
print("Name:", student["name"])
print("Age:", student["age"])

#Add a new course to the student's dictionary.
student = {
    "name": "Vignesh",
    "age": 24
}
student["course"] = "Python"
print(student)

#Change the student's age in the dictionary.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python"
}
student["age"] = 25
print(student)

#Remove the age from the student's dictionary.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python"
}
student.pop("age")
print(student)

#Check whether the student's course is available in the dictionary.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python"
}
if "course" in student:
    print("Course is available")
else:
    print("Course is not available")

#Print all the keys from the student's dictionary.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python"
}
for key in student:
    print(key)

#Print all the values from the student's dictionary.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python"
}
for value in student.values():
    print(value)

#Find how many details are stored in the student's dictionary.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python",
    "city": "Amalapuram"
}
print("Total details:", len(student))

#Print each student detail along with its value.
student = {
    "name": "Vignesh",
    "age": 24,
    "course": "Python",
    "city": "Amalapuram"
}
for key, value in student.items():
    print(key, ":", value)