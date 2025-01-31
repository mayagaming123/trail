import math

def calculate_emi(principal, rate, time):
    """Calculates Equated Monthly Installment (EMI).

    Args:
        principal: The principal loan amount.
        rate: The annual interest rate (as a decimal, e.g., 0.10 for 10%).
        time: The loan tenure in months.

    Returns:
        The EMI amount. Returns a string with an error message if inputs are invalid.
    """
    if principal <= 0 or rate <= 0 or time <= 0:
       return "Invalid input: Principal, rate, and time must be positive."

    # Monthly interest rate
    r = rate / 12

    # EMI calculation formula
    try:
        emi = (principal * r * (1 + r)**time) / ((1 + r)**time - 1)
        return emi
    except OverflowError: #Handles potential overflow issues for very large numbers
        return "Overflow Error: Inputs are too large for calculation."
    except ZeroDivisionError: #Handles a Zero Division Error
        return "Zero Division Error: Please check your inputs."



# Get input from the user
try:
    principal = float(input("Enter the principal loan amount: "))
    rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.10 for 10%): "))
    time = int(input("Enter the loan tenure in months: "))  # Time is usually in months
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()  # Exit the program if input is invalid


emi = calculate_emi(principal, rate, time)

if isinstance(emi, str): #Checks if the returned value is a string (error message)
    print(emi)
else:
    print(f"The EMI is: {emi:.2f}") #Formats the EMI to two decimal places

# Example Usage (you can uncomment these for testing)
# print(calculate_emi(100000, 0.10, 12))  # Example: 8791.59
# print(calculate_emi(500000, 0.08, 24))  # Example: 22224.44
# print(calculate_emi(1000, 0.05, 36)) # Example: 29.97
# print(calculate_emi(0, 0.10, 12))  # Example: Invalid input: Principal, rate, and time must be positive.
# print(calculate_emi(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000