price = int(input("enter the price: "))
premium_membership = True
if price >= 1000 or premium_membership:
    print("provides free delivary")
else:
    print("does not provides any free delivary")