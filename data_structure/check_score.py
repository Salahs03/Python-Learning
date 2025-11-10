scores = {"Alice": 75, "Bob": 50, "Charlie": 90}

def print_passed():
    for student, score in scores.items():
        if score >= 60:
            print(student, "passed")

print_passed()

# This code prints students who passed based on their scores