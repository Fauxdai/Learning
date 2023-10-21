weight = float(input("Weight of Package: "))

#----- Ground Shipping -----

if weight <= 2:
    price = 4.50
    print("Your price is: $", price * weight + 20)
elif weight > 2 and weight <= 6:
    price = 3.00
    print("Your price is: $", price * weight + 20)
elif weight > 6:
    price = 4.00
    print("Your price is: $", price * weight + 20)
else:
    price = 4.75
    print("Your price is: $", price * weight + 20)