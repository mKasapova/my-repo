N1 = int(input())
N2 = int(input())
operator = input()
res = 0

if operator == "+":
    res = N1 + N2
elif operator == "-":
    res = N1 - N2
elif operator == "*":
    res = N1 * N2
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        res = N1 / N2
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        res = N1 % N2

if operator in ("+", "-", "*"):
    if res % 2 == 0:
        print(f"{N1} {operator} {N2} = {res} - even")
    else:
        print(f"{N1} {operator} {N2} = {res} - odd")
elif operator == "/" and N2 != 0:
    print(f"{N1} / {N2} = {res:.2f}")
elif operator == "%" and N2 != 0:
    print(f"{N1} % {N2} = {res}")