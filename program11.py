def find_multiples(number, n):
    """Finds the first n multiples of a given number.

    Args:
        number: The number for which to find multiples.
        n: The number of multiples to find.

    Returns:
        A list containing the first n multiples of the given number, 
        or an appropriate error message if the input is invalid.
    """

    if not isinstance(number, (int, float)):
        return "Invalid input: Number must be a number (int or float)."

    if not isinstance(n, int) or n <= 0:
        return "Invalid input: n must be a positive integer."

    multiples = []
    for i in range(1, n + 1):
        multiple = number * i
        multiples.append(multiple)

    return multiples


# Example Usage:
number = 7
n = 5
multiples = find_multiples(number, n)

if isinstance(multiples, str): #Check if the returned value is a string (error message)
    print(multiples)
else:
    print(f"The first {n} multiples of {number} are: {multiples}")  # Output: [7, 14, 21, 28, 35]

# Example Usage with error handling:
multiples2 = find_multiples(7, -5)
print(multiples2)

multiples3 = find_multiples("abc", 5)
print(multiples3)