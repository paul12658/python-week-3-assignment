def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it is 20% or higher.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The discounted price if applicable, or the original price otherwise.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"The final price after the discount is: KSH{final_price:.2f}")
else:
    print(f"No discount applied. The original price is: KSH{original_price:.2f}")
