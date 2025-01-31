def count_alphabet_occurrences(strings, alphabet):
    """
    Counts the number of occurrences of a given alphabet in each string within a list of strings.

    Args:
        strings: A list of strings.
        alphabet: The alphabet to count occurrences for.

    Returns:
        A list where each element is the count of the given alphabet in the corresponding string.
        Returns an error message if the inputs are invalid.
    """

    if not isinstance(strings, list):
        return "Invalid input: strings must be a list."

    if not isinstance(alphabet, str) or len(alphabet) != 1 or not alphabet.isalpha():
        return "Invalid input: alphabet must be a single alphabetic character."

    counts = []
    for string in strings:
        if not isinstance(string, str):
            return "Invalid input: All elements in the strings list must be strings."

        count = 0
        for char in string:
            if char.lower() == alphabet.lower():
                count += 1
        counts.append(count)

    return counts


# Example usage:
strings = ["apple", "banana", "cherry", "date"]
alphabet = "a"
occurrences = count_alphabet_occurrences(strings, alphabet)

if isinstance(occurrences, str): #Checks if the returned value is a string (error message)
    print(occurrences)
else:
    print(f"Occurrences of '{alphabet}': {occurrences}")

strings2 = ["apple", "banana", "cherry", "date"]
alphabet2 = 123
occurrences2 = count_alphabet_occurrences(strings2, alphabet2)
print(occurrences2)

strings3 = ["apple", "banana", "cherry", "date"]
alphabet3 = "ab"
occurrences3 = count_alphabet_occurrences(strings3, alphabet3)
print(occurrences3)

strings4 = ["apple", 123, "cherry", "date"]
alphabet4 = "a"
occurrences4 = count_alphabet_occurrences(strings4, alphabet4)
print(occurrences4)