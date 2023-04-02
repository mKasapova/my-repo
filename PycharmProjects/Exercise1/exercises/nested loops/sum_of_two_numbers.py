n = int(input())
m = int(input())
magic_number = int(input())
count = 0
sum = 0

for x in range(n, m + 1):
    found = False
    for y in range(n, m + 1):
        count += 1
        sum = x + y
        if sum == magic_number:
            print(f"Combination N:{count} ({x} + {y} = {magic_number})")
            found = True
            break
        else:
            continue
    if found:
        break

if sum != magic_number:
    print(f"{count} combinations - neither equals {magic_number}")