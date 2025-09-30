def check_password(password):
    if len(password) < 6:          # Check if the password is shorter than 6 characters
        return "Weak: too short"
    elif password.isalpha():         # Check if the password contains only letters and numbers (no symbols)
        return "Weak: only letters"
    elif password.isalnum():         # If the password contains letters, numbers, and at least one symbol
        return "Medium: letters and numbers"
    else:
        return "Strong: letters, numbers, and symbols"


# Example usage
print(check_password("hello"))
print(check_password("hellooo"))
print(check_password("hello123"))
print(check_password("hello123!"))
