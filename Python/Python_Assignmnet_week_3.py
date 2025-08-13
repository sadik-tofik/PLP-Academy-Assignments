def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    return price

price = int(input("Enter the price of the item: "))
discount = int(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount)
print("The final price is:", final_price)