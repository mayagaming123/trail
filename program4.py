def simple_interest(principal, rate, time):
    """Calculates simple interest.

    Args:
        principal: The principal amount.
        rate: The annual interest rate (as a decimal).
        time: The time in years.

    Returns:
        The simple interest.
    """
    si = (principal * rate * time)
    return si


def compound_interest(principal, rate, time, n):
    """Calculates compound interest.

    Args:
        principal: The principal amount.
        rate: The annual interest rate (as a decimal).
        time: The time in years.
        n: The number of times interest is compounded per year.

    Returns:
        The compound interest.
    """

    amount = principal * (1 + (rate / n)) ** (n * time)
    ci = amount - principal
    return ci



# Get input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
time = float(input("Enter the time in years: "))

# For compound interest, get the compounding frequency
compounding_frequency = input("Enter the compounding frequency (e.g., 'annually', 'quarterly', 'monthly', 'daily'): ").lower()

if compounding_frequency == "annually":
    n = 1
elif compounding_frequency == "quarterly":
    n = 4
elif compounding_frequency == "monthly":
    n = 12
elif compounding_frequency == "daily":
    n = 365
else:
    print("Invalid compounding frequency. Assuming annually.")
    n = 1


# Calculate and print the results
simple_interest_amount = simple_interest(principal, rate, time)
compound_interest_amount = compound_interest(principal, rate, time, n)

print(f"Simple Interest: {simple_interest_amount}")
print(f"Compound Interest: {compound_interest_amount}")


# Example Usage (you can uncomment these for testing)
# print(simple_interest(1000, 0.05, 2))  # Output: 100.0
# print(compound_interest(1000, 0.05, 2, 1)) # Output: 102.5
# print(compound_interest(1000, 0.05, 2, 4)) # Output: 104.94506250000004