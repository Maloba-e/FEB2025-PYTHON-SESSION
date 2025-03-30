def calculate_discount(price,discount_percent):
    price = int(input('Enter the original price:'))
    discount_percent = int(input('Enter the discount percent:'))
    final_price = price - (price * discount_percent) / 100
    if discount_percent >=20:
        print(f"Discount of {discount_percent}% is applied") 
        return f"The final price = {final_price}"
    else:
        print("No discount was applied")
        return f"The final price is = {price}"
    
print(calculate_discount("","")) 

    
    
# def my_math(a,b):
#     sum= a+b
#     return sum
# my_math(1,2)