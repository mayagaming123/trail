def create_state_capital_dictionary():
    """Creates a dictionary to store state names and their capitals.

    Returns:
        A dictionary where keys are state names and values are their capitals.
        Returns an empty dictionary if there are any issues during input.
    """

    state_capital_dict = {}

    while True:
        state = input("Enter a state name (or type 'done' to finish): ")
        if state.lower() == "done":
            break

        capital = input(f"Enter the capital of {state}: ")

        if not state or not capital: #Check for empty input
            print("State and capital cannot be empty. Please try again.")
            continue #Go back to the beginning of the loop

        if state.lower() in (existing_state.lower() for existing_state in state_capital_dict): #Check for duplicate entries (case-insensitive)
            print(f"State '{state}' already exists in the dictionary.")
            continue

        state_capital_dict[state] = capital

    return state_capital_dict


def print_state_capital_dictionary(state_capital_dict):
    """Prints the state and capital dictionary in a formatted way.

    Args:
        state_capital_dict: The dictionary to print.
    """
    if not state_capital_dict:
        print("The dictionary is empty.")
        return

    print("\nState and Capital Information:")
    for state, capital in state_capital_dict.items():
        print(f"{state}: {capital}")


# Create the dictionary
state_capital_dictionary = create_state_capital_dictionary()

# Print the dictionary
print_state_capital_dictionary(state_capital_dictionary)



# Example of how to access a capital:
if state_capital_dictionary: #Check if dictionary is not empty before trying to access elements
    state_name = input("Enter a state to find its capital: ")
    if state_name in state_capital_dictionary:
        print(f"The capital of {state_name} is {state_capital_dictionary[state_name]}.")
    else:
        print(f"{state_name} not found in the dictionary.")