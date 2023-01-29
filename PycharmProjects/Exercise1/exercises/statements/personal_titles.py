years = float(input())
gender = input()

if gender == "m":
    if years >= 16:
        print("Mr.")
    else:
        print("Master")
if gender == "f":
    if years >= 16:
        print("Ms.")
    else:
        print("Miss")