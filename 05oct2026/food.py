price = int(input("enter the price: "))
quantity = int(input("enter the quantity: "))
delivary_charge = int(input("enter the delivary_charge: "))
discount_percentage = float(input("enter the discount_percentage: "))
final_bill = (price*quantity+delivary_charge)- discount_percentage

print(final_bill)