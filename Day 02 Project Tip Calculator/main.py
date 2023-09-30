bill = float(input("Enter the total bill: $"))
tip = int(input("Percentage of tip you want to give: "))
people = int(input("Bill split among: "))
payment = ((tip/100) * bill) + bill
payment_each = "{:.2f}".format(payment / people)

print(f"Each person should pay: {payment_each}")