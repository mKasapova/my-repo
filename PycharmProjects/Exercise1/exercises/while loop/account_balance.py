total = 0

while True:
    sum = input()
    if sum == "NoMoreMoney":
        break
    if float(sum) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(sum):.2f}")
    total += float(sum)

print(f"Total: {total:.2f}")