# gym_age_checker.py

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check if the user is too young
if age < 16:
    print("Too young for a gym membership.")
# Check if the user is in the standard age range
elif age <= 65:
    print("You can get a standard gym membership!")
# If the user is older than 65
else:
    print("You can get a senior gym membership!")
