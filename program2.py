def calculate_sales_price(cost_price, discount_percentage):
    """
    Calculates the sales price of an item after applying a discount.

    Args:
        cost_price: The original cost of the item.
        discount_percentage: The discount percentage (e.g., 20 for 20%).

    Returns:
        The sales price of the item, or a message if the input is invalid.
    """

    if cost_price < 0:
        return "Cost price cannot be negative."
    if discount_percentage < 0 or discount_percentage > 100:
        return "Discount percentage must be between 0 and 100."

    discount_amount = (discount_percentage / 100) * cost_price
    sales_price = cost_price - discount_amount
    return sales_price


# Get input from the user (optional - you can set the values directly)
try:
    cost_price = float(input("Enter the cost price: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    sales_price = calculate_sales_price(cost_price, discount_percentage)

    if isinstance(sales_price, str):  # Check if it's an error message
        print(sales_price)
    else:
        print("Sales price:", sales_price)

except ValueError:
    print("Invalid input. Please enter numeric values.")



# Example usage (without user input)
cost = 100
discount = 20
sales_price = calculate_sales_price(cost, discount)
print(f"Cost: {cost}, Discount: {discount}%, Sales Price: {sales_price}")

cost = 50
discount = 0
sales_price = calculate_sales_price(cost, discount)
print(f"Cost: {cost}, Discount: {discount}%, Sales Price: {sales_price}")


cost = 200
discount = 50
sales_price = calculate_sales_price(cost, discount)
print(f"Cost: {cost}, Discount: {discount}%, Sales Price: {sales_price}")

#Example of error handling
cost = -10
discount = 20
sales_price = calculate_sales_price(cost, discount)
print(f"Cost: {cost}, Discount: {discount}%, Sales Price: {sales_price}")

cost = 100
discount = 110
sales_price = calculate_sales_price(cost, discount)
print(f"Cost: {cost}, Discount: {discount}%, Sales Price: {sales_price}")