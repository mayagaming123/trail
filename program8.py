def find_min_max(numbers):
    """Finds the smallest and largest numbers in a list.

    Args:
        numbers: A list of numbers.

    Returns:
        A tuple containing the smallest and largest numbers in the list.
        Returns an appropriate message if the input is invalid or empty.
    """

    if not isinstance(numbers, list):  # Check if it's a list
        return "Invalid input: Input must be a list."

    if not numbers:  # Check if the list is empty
        return "Empty list: Cannot find min/max of an empty list."


    min_num = numbers[0]  # Initialize with the first element
    max_num = numbers[0]

    for number in numbers:
        if not isinstance(number, (int, float)): #Check if all elements are numbers
            return "Invalid input: List elements must be numbers."
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number

    return min_num, max_num



# Example Usage:
numbers = [5, 2, 9, 1, 5, 6]
smallest, largest = find_min_max(numbers)

if isinstance(smallest, str): #Checks if the returned value is a string (error message)
    print(smallest)
else:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")


numbers2 = []
smallest2, largest2 = find_min_max(numbers2)
print(smallest2)

numbers3 = [5, 2, "a", 1, 5, 6]
smallest3, largest3 = find_min_max(numbers3)
print(smallest3)

numbers4 = 123
smallest4, largest4 = find_min_max(numbers4)
print(smallest4)