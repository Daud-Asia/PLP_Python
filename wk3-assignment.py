1.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

2.
#Prompt user for inputs
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

#Call the function
final_price = calculate_discount(price, discount)

#Output the result
if discount >= 20:
    print(f"Discount applied. Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")


