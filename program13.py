def find_words_starting_with(text, alphabet):
    """Finds all words in a given text that start with a specific alphabet (case-insensitive).

    Args:
        text: The input string.
        alphabet: The alphabet to search for (case-insensitive).

    Returns:
        A list of words that start with the given alphabet, or an empty list if no such words are found.
        Returns an error message if the inputs are invalid.
    """

    if not isinstance(text, str):
        return "Invalid input: Text must be a string."

    if not isinstance(alphabet, str) or len(alphabet) != 1 or not alphabet.isalpha():
        return "Invalid input: Alphabet must be a single alphabetic character."

    words = text.split()  # Split the text into a list of words
    result = []

    for word in words:
        if word.lower().startswith(alphabet.lower()):  # Case-insensitive comparison
            result.append(word)

    return result


# Get input from the user
user_string = input("Enter a string: ")
starting_alphabet = input("Enter the alphabet to search for: ")


words_starting_with = find_words_starting_with(user_string, starting_alphabet)

if isinstance(words_starting_with, str): #Checks if the returned value is a string (error message)
    print(words_starting_with)
elif words_starting_with:  # Check if the list is not empty before printing
    print(f"Words starting with '{starting_alphabet}': {words_starting_with}")
else:
    print(f"No words found starting with '{starting_alphabet}'.")


# Example Usage (you can uncomment these for testing)
# print(find_words_starting_with("This is a Sample sentence to test the function.", "s"))  # Output: ['Sample', 'sentence']
# print(find_words_starting_with("Hello World", "z"))  # Output: []
# print(find_words_starting_with("Apple Banana Orange", "a"))  # Output: ['Apple']
# print(find_words_starting_with("apple Banana Orange", "A"))  # Output: ['apple']
# print(find_words_starting_with(123, "A")) #Output: Invalid input: Text must be a string.
# print(find_words_starting_with("apple Banana Orange", "AB")) #Output: Invalid input: Alphabet must be a single alphabetic character.