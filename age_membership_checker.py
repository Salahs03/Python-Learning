# Check user's age and membership type
age = 25
membership = "premium"

if age < 18:
    print("Sorry, you must be 18 or older.")
elif membership == "premium":
    print("Welcome, premium member! Enjoy your benefits.")
elif membership == "basic":
    print("Welcome, basic member! Consider upgrading for perks.")
else:
    print("Membership type unknown. Please contact support.")

# Extra condition using logical operators
if age >= 18 and membership == "premium":
    print("You qualify for our exclusive events!")
