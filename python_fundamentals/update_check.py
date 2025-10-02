# Existing dictionary
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Update Bob's score
student_scores["Bob"] = 95

# Check if a student exists in the dictionary
if "Alice" in student_scores:
    print("Alice's score is:", student_scores["Alice"])

# Try checking a non-existing key
if "David" not in student_scores:
    print("David is not in the dictionary yet.")
