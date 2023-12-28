def store_strings():
    strings_list = []  # Initialize an empty list to store strings

    # Get user input for strings until the user enters an empty string
    while True:
        user_input = input("Enter a string (press Enter to finish): ")
        if not user_input:
            break  # Break the loop if the user enters an empty string
        strings_list.append(user_input)

    return strings_list

def print_strings(strings_list):
    print("Stored Strings:")
    for string in strings_list:
        print(string)

# Store strings
stored_strings = store_strings()

# Print stored strings
print_strings(stored_strings)
