fruit = input()
day = input()
quantity = float(input())
price = 0

if day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    if fruit == "banana":
        price = quantity * 2.50
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = quantity * 1.20
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = quantity * 0.85
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = quantity * 1.45
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = quantity * 2.70
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = quantity * 5.50
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = quantity * 3.85
        print(f"{price:.2f}")
    else:
        print("error")
elif day in ("Saturday", "Sunday"):
    if fruit == "banana":
        price = quantity * 2.70
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = quantity * 1.25
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = quantity * 0.90
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = quantity * 1.60
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = quantity * 3.00
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = quantity * 5.60
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = quantity * 4.20
        print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")

