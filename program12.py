def count_vowels(text):
    """Counts the number of vowels (a, e, i, o, u) in a string.
    Case-insensitive.

    Args:
        text: The input string.

    Returns:
        The number of vowels in the string.
    """

    vowel_count = 0
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)

    for char in text:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Get input from the user
user_string = input("Enter a string: ")

# Count the vowels
num_vowels = count_vowels(user_string)

# Print the result
print(f"The string '{user_string}' contains {num_vowels} vowels.")



# Example Usage (you can uncomment these for testing)
# print(count_vowels("Hello, World!"))  # Output: 3
# print(count_vowels("Python Programming"))  # Output: 4
# print(count_vowels("12345"))  # Output: 0