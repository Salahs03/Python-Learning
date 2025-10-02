def check_grade(name, score):            # Function checks grade and returns result
    name = name.capitalize()             # Format the name nicely
    if score >= 70:
        return f"{name} passed with {score}!"
    elif score >= 50:
        return f"{name} just scraped a pass with {score}."
    else:
        return f"{name} failed with {score}."

print(check_grade("alice", 85))          # Call the function with arguments
print(check_grade("bob", 52))
print(check_grade("charlie", 40))



# numbers + categories + formatted output