def find_highest_lowest(dictionary):
    """Finds the highest and lowest values in a dictionary.

    Args:
        dictionary: The input dictionary (values should be comparable).

    Returns:
        A tuple containing the highest and lowest values.
        Returns an appropriate message if the input is invalid or empty.
    """

    if not isinstance(dictionary, dict):
        return "Invalid input: Input must be a dictionary."

    if not dictionary:  # Check if the dictionary is empty
        return "Empty dictionary: Cannot find min/max of an empty dictionary."

    values = list(dictionary.values())  # Get a list of the dictionary's values

    if not all(isinstance(x, (int, float)) for x in values): #Check if all values are numbers
            return "Invalid input: Dictionary values must be numbers."

    highest = max(values)
    lowest = min(values)

    return highest, lowest



# Example usage:
my_dict = {"a": 10, "b": 5, "c": 20, "d": 15}
highest_value, lowest_value = find_highest_lowest(my_dict)

if isinstance(highest_value, str): #Checks if the returned value is a string (error message)
    print(highest_value)
else:
    print(f"Highest value: {highest_value}")
    print(f"Lowest value: {lowest_value}")

my_dict2 = {}
highest_value2, lowest_value2 = find_highest_lowest(my_dict2)
print(highest_value2)

my_dict3 = {"a": 10, "b": "abc", "c": 20, "d": 15}
highest_value3, lowest_value3 = find_highest_lowest(my_dict3)
print(highest_value3)

my_dict4 = 123
highest_value4, lowest_value4 = find_highest_lowest(my_dict4)
print(highest_value4)