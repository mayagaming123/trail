def calculate_gst(amount, gst_rate):
    """Calculates Goods and Services Tax (GST).

    Args:
        amount: The original amount before GST.
        gst_rate: The GST rate as a decimal (e.g., 0.18 for 18%).

    Returns:
        A tuple containing the GST amount and the total amount (including GST), or an error message if inputs are invalid.
    """
    if amount < 0 or gst_rate < 0:
        return "Invalid input: Amount and GST rate must be non-negative."

    gst_amount = amount * gst_rate
    total_amount = amount + gst_amount
    return gst_amount, total_amount


def calculate_income_tax(income, tax_slabs):
    """Calculates income tax based on provided tax slabs.

    Args:
        income: The taxable income.
        tax_slabs: A dictionary representing tax slabs. Keys are income thresholds,
                   and values are the corresponding tax rates (as decimals).  
                   Slabs should be ordered from lowest to highest income.
                   A final "default" or "highest" slab *must* be included.

    Returns:
        The calculated income tax amount, or an error message if inputs are invalid.
    """

    if income < 0:
        return "Invalid input: Income must be non-negative."

    tax = 0
    remaining_income = income

    for slab_income, rate in tax_slabs.items():
        if remaining_income <= 0:  # No more income to tax
            break
        if isinstance(slab_income, str) and slab_income.lower() == "default": #Handles the default/highest slab.
            tax += remaining_income * rate
            break
        if remaining_income > slab_income:
            tax += slab_income * rate  # Tax the income within the current slab
            remaining_income -= slab_income  # Deduct the income already taxed
        else:
            tax += remaining_income * rate  # Tax the remaining income in the current slab
            remaining_income = 0

    return tax




# --- Example GST Calculation ---
try:
    amount = float(input("Enter the amount before GST: "))
    gst_rate = float(input("Enter the GST rate (as a decimal, e.g., 0.18 for 18%): "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

gst_amount, total_amount = calculate_gst(amount, gst_rate)
if isinstance(gst_amount, str): #Checks if the returned value is a string (error message)
    print(gst_amount)
else:
    print(f"GST Amount: {gst_amount:.2f}")
    print(f"Total Amount (including GST): {total_amount:.2f}")



# --- Example Income Tax Calculation ---

tax_slabs = {
    0: 0.0,       # 0% tax up to this amount
    250000: 0.05,  # 5% tax up to this amount
    500000: 0.20,  # 20% tax up to this amount
    1000000: 0.30, # 30% tax up to this amount
    "default": 0.40 #40% for anything above the last specified slab
}


try:
    income = float(input("Enter your taxable income: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

income_tax = calculate_income_tax(income, tax_slabs)

if isinstance(income_tax, str): #Checks if the returned value is a string (error message)
    print(income_tax)
else:
    print(f"Income Tax: {income_tax:.2f}")