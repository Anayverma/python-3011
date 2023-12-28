def sqrt_without_builtin(number, num_iterations=100):
    guess = number / 2.0
    for _ in range(num_iterations):
        guess = (guess + number / guess) / 2.0
    return guess
# Example usage:
number = 24
result = sqrt_without_builtin(number)
print(f"The square root of {number} is approximately {result}")
print(number**0.5)