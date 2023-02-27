moves = int(input())
result = 0
numbers = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for i in range(0, moves):
    numbers.append(int(input()))

for i in range(0, len(numbers)):
    if 0 <= numbers[i] <= 9:
        count2 += 1
        result = result + numbers[i] * 0.2
    elif 10 <= numbers[i] <= 19:
        count3 += 1
        result = result + numbers[i] * 0.3
    elif 20 <= numbers[i] <= 29:
        count4 += 1
        result = result + numbers[i] * 0.4
    elif 30 <= numbers[i] <= 39:
        count5 += 1
        result = result + 50
    elif 40 <= numbers[i] <= 50:
        count6 += 1
        result = result + 100
    else:
        count1 += 1
        result = result / 2

print(f"{result:.2f}")
print(f"From 0 to 9: {((count2 / moves) * 100):.2f}%")
print(f"From 10 to 19: {((count3 / moves) * 100):.2f}%")
print(f"From 20 to 29: {((count4 / moves) * 100):.2f}%")
print(f"From 30 to 39: {((count5 / moves) * 100):.2f}%")
print(f"From 40 to 50: {((count6 / moves) * 100):.2f}%")
print(f"Invalid numbers: {((count1 / moves) * 100):.2f}%")