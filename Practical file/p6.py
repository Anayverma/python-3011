def get_user_input():
    return input("Enter your username: ")

def verify_data(username):
    if len(username) != 0 :
        return True
    else:
        return False

def welcome_user(username):
    print(f"Welcome, {username}!")

# Get user input
user_input = get_user_input()

# Verify data
if verify_data(user_input):
    # If data is valid, welcome the user
    welcome_user(user_input)
else:
    # If data is not valid, print an error message
    print("Invalid input. Please enter a valid username.")
