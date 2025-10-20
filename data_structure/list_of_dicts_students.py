# A list containing multiple dictionaries
students = [
    {"name": "Alice", "age": 10, "grade": "A"},
    {"name": "Bob", "age": 11, "grade": "B"},
    {"name": "Charlie", "age": 10, "grade": "A"}
]

# Looping through the list of dictionaries
for student in students:
    print(student["name"], "is", student["age"], "years old and got grade", student["grade"])

# Accessing a specific value
print("Second student’s name:", students[1]["name"])

