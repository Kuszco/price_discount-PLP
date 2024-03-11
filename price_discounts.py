def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * discount_percent / 100
        final_price = price - discount
    else:
        final_price = price
    return final_price
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage(0 to 100): "))
final_price = calculate_discount (original_price, discount_percent)
print(f"Final price after discount: ${final_price:0.2f}")