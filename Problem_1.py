import re

def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special symbol."
    if not re.search(r'\d', password):
        return "Password must contain at least one number."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    return None

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not re.match(pattern, email):
        return "Invalid email address."
    return None

def main():
    print("Menu")
    print("1. Enter Username")
    print("2. Enter Password")
    print("3. Enter Email")
    print("4. Exit")
    
    username = input("Enter Username: ")
    username_error = validate_username(username)
    if username_error:
        print(f"Error: {username_error}")
        return
    
    password = input("Enter Password: ")
    password_error = validate_password(password)
    if password_error:
        print(f"Error: {password_error}")
        return

    email = input("Enter Email: ")
    email_error = validate_email(email)
    if email_error:
        print(f"Error: {email_error}")
        return

    print("All inputs are valid!")

if __name__ == "__main__":
    main()
