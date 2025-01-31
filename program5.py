def calculate_profit_loss(cost_price, selling_price):
    """Calculates profit or loss.

    Args:
        cost_price: The cost price of the item.
        selling_price: The selling price of the item.

    Returns:
        A tuple containing:
        - A string indicating "Profit" or "Loss" or "No Profit/Loss".
        - The profit or loss amount (0 if no profit/loss).
    """

    if selling_price > cost_price:
        profit = selling_price - cost_price
        return "Profit", profit
    elif selling_price < cost_price:
        loss = cost_price - selling_price
        return "Loss", loss
    else:
        return "No Profit/Loss", 0.0  # Return 0.0 for the amount in this case


# Get input from the user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate profit/loss
result, amount = calculate_profit_loss(cost_price, selling_price)

# Print the result
print(f"Result: {result}")
if result != "No Profit/Loss":  # Only print the amount if there was a profit or loss
    print(f"Amount: {amount}")


# Example Usage (you can uncomment these for testing)
# print(calculate_profit_loss(10, 15))  # Output: ('Profit', 5)
# print(calculate_profit_loss(15, 10))  # Output: ('Loss', 5)
# print(calculate_profit_loss(10, 10))  # Output: ('No Profit/Loss', 0.0)