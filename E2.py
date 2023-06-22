name = input("Name: ").upper()
appleconf = str(input("Do you want to buy Apples? 20.00 per piece. ").lower())
apple = 0
appletot = 0
if appleconf == "yes":
    apple = int(input("How many will you buy? "))
    appletot = (apple * 20)
mangoconf = str(input("Do you want to buy Mangoes? 15.00 per piece. ").lower())
mango = 0
mangotot = 0
if mangoconf == "yes":
    mango = int(input("How many will you buy? "))
    mangotot = (mango * 15)
orangeconf = str(input("Do you want to buy Oranges? 10.00 per piece. ").lower())
orange = 0
orangetot = 0
if orangeconf == "yes":
    orange = int(input("How many will you buy? "))
    orangetot = (orange * 10)
print()

#total of purchase
total = int(appletot + mangotot + orangetot)

#display the receipt (with discount)
if total > 200:
    discount = (total * .20)
    totald = total - discount
    print(f"""Apple x{apple} ---------- {appletot}
Mango x{mango} ---------- {mangotot}
Orange x{orange} ---------- {orangetot}
==============================
Total ---------- {total}

Hello {name}!
Total payment ---------- {totald}
Discount ---------- {discount}""")
    cash = int(input("Cash Tendered ---------- "))
    while cash < totald:
        cash = int(input("The value is insufficient. Please try again. "))
    print("Change ---------- " + str(cash - totald) + "\n\nThank you for Buying!")
#receipt (no discount)
else:
    print(f"""Apple x{apple} ---------- {appletot}
Mango x{mango} ---------- {mangotot}
Orange x{orange} ---------- {orangetot}
==============================
Total ---------- {total}

Hello {name}!
Total payment ---------- {total}""")
    cash = int(input("Cash Tendered ---------- "))
    while cash < total:
        cash = int(input("The value is insufficient. Please try again. "))
    print("Change ---------- " + str(cash - total) + "\n\nThank you for Buying!")