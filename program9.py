def find_kth_largest_smallest(numbers, k, largest=True):
    """Finds the k-th largest or smallest number in a list.

    Args:
        numbers: A list of numbers.
        k: The k-th element to find (e.g., k=3 for the 3rd largest).
        largest: A boolean indicating whether to find the k-th largest (True)
                 or k-th smallest (False) element. Defaults to True (largest).

    Returns:
        The k-th largest or smallest number, or an appropriate message if the input is invalid.
    """

    if not isinstance(numbers, list):
        return "Invalid input: Input must be a list."

    if not numbers:
        return "Empty list: Cannot find k-th element of an empty list."

    if not isinstance(k, int) or k <= 0:
        return "Invalid input: k must be a positive integer."

    if k > len(numbers):
        return "Invalid input: k is larger than the list length."

    if not all(isinstance(x, (int, float)) for x in numbers):
        return "Invalid input: All list elements must be numbers."


    # Create a copy to avoid modifying the original list
    sorted_numbers = sorted(numbers, reverse=largest)  # Sort in descending order for largest, ascending for smallest

    return sorted_numbers[k - 1]  # k is 1-based indexing



# Example Usage (3rd largest):
numbers = [5, 2, 9, 1, 5, 6, 12, 3]
third_largest = find_kth_largest_smallest(numbers, 3)

if isinstance(third_largest, str):  # Check for error messages
    print(third_largest)
else:
    print(f"The 3rd largest number is: {third_largest}")  # Output: 6

# Example Usage (2nd smallest):
second_smallest = find_kth_largest_smallest(numbers, 2, largest=False)
if isinstance(second_smallest, str):  # Check for error messages
    print(second_smallest)
else:
    print(f"The 2nd smallest number is: {second_smallest}") # Output: 2

#Example of error handling
numbers2 = [5, 2, "a", 1, 5, 6, 12, 3]
third_largest2 = find_kth_largest_smallest(numbers2, 3)
print(third_largest2)

numbers3 = [5, 2, 9, 1, 5, 6, 12, 3]
third_largest3 = find_kth_largest_smallest(numbers3, 10)
print(third_largest3)

numbers4 = 123
third_largest4 = find_kth_largest_smallest(numbers4, 3)
print(third_largest4)