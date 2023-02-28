n = int(input())
numbers = []
values = []
diff = 0
value = 0
max_diff = 0

for i in range(0, 2 * n):
    numbers.append(int(input()))

for i in range(0, len(numbers) - 1, 2):
    value = numbers[i] + numbers[i+1]
    values.append(value)

for i in range(0, len(values)-1):
    if values[i] != values[i+1]:
        diff = abs(values[i] - values[i+1])
        if diff > max_diff:
            max_diff = diff

if max_diff == 0:
    print(f"Yes, value={values[0]}")
else:
    print(f"No, maxdiff={max_diff}")