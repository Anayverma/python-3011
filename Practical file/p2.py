# Get user input for the limit 'n'
n = int(input("Enter Value of n --> "))
prime_num = []  # List to store prime numbers

# Iterate through numbers from 2 to (n-1)
for num in range(1, n+1):
    count = 0  # Counter to check if the number is prime
    # Check for divisors from 2 to the square root of 'num' + 1
    for i in range(2, int (num**0.5) + 1):
        if num % i == 0:
            count = 1  # Set count to 1 if 'num' is not prime
            break  # Exit the loop if a divisor is found
    if count == 0 and num != 1 :
        prime_num.append(num)  # Add 'num' to the list if it's prime

# Print the list of prime numbers
print("Prime Numbers up to", n, ":", prime_num)
