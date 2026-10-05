cash = int(input("enter the cash: "))
balance = int(input("enter the balance: "))

if cash<= balance and cash // 500:
    print("transaction allowed")
else:
    print("transaction not allowed")