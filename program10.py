def sum_of_squares(n):
    """Calculates the sum of squares of the first n natural numbers.

    Args:
        n: The number of natural numbers to consider (must be a positive integer).

    Returns:
        The sum of squares, or an error message if the input is invalid.
    """

    if not isinstance(n, int) or n <= 0:
        return "Invalid input: n must be a positive integer."

    sum_sq = 0
    for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
        sum_sq += i**2  # or i*i

    return sum_sq

# Calculate the sum of squares of the first 100 natural numbers
n = 100
result = sum_of_squares(n)

if isinstance(result, str): #Check if the returned value is a string (error message)
    print(result)
else:
    print(f"The sum of squares of the first {n} natural numbers is: {result}")  # Output: 338350

# Example usage with error handling:
result2 = sum_of_squares(-5)
print(result2)

result3 = sum_of_squares("abc")
print(result3)