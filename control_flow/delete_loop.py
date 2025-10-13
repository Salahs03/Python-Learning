# Existing dictionary
student_scores = {"Alice": 85, "Bob": 95, "Charlie": 78}

# Delete Charlie's entry
del student_scores["Charlie"]

# Loop through dictionary and print each student and score
for student, score in student_scores.items():
    print(f"{student}: {score}")
