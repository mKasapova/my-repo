city = input()
sellings = float(input())
commision = 0

if city == "Sofia":
    if 0 <= sellings <= 500:
        commision = sellings * 0.05
        print(f"{commision:.2f}")
    elif 500 < sellings <= 1000:
        commision = sellings * 0.07
        print(f"{commision:.2f}")
    elif 1000 < sellings <= 10_000:
        commision = sellings * 0.08
        print(f"{commision:.2f}")
    elif sellings > 10_000:
        commision = sellings * 0.12
        print(f"{commision:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sellings <= 500:
        commision = sellings * 0.045
        print(f"{commision:.2f}")
    elif 500 < sellings <= 1000:
        commision = sellings * 0.075
        print(f"{commision:.2f}")
    elif 1000 < sellings <= 10_000:
        commision = sellings * 0.10
        print(f"{commision:.2f}")
    elif sellings > 10_000:
        commision = sellings * 0.13
        print(f"{commision:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sellings <= 500:
        commision = sellings * 0.055
        print(f"{commision:.2f}")
    elif 500 < sellings <= 1000:
        commision = sellings * 0.08
        print(f"{commision:.2f}")
    elif 1000 < sellings <= 10_000:
        commision = sellings * 0.12
        print(f"{commision:.2f}")
    elif sellings > 10_000:
        commision = sellings * 0.145
        print(f"{commision:.2f}")
    else:
        print("error")
else:
    print("error")

