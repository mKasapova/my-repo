n = int(input())
if n == 0:
    print("OddSum=0.00,")
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No")
    exit()

numbers = []
odd = []
even = []

for i in range(0, n):
    numbers.append(float(input()))

maxi = 1000000000.0
mini = -1000000000.0
odd_sum = numbers[0]
odd.insert(0, numbers[0])
even_sum = 0
odd_maximum = maxi
odd_minimum = mini
even_maximum = maxi
even_minimum = mini

for i in range(1, len(numbers)):
    if i % 2 == 0:
        odd_sum += numbers[i]
        odd.append(numbers[i])
    else:
        even_sum += numbers[i]
        even.append(numbers[i])

if len(odd) != 0:
    odd_maximum = max(odd)
    odd_minimum = min(odd)
if len(even) != 0:
    even_maximum = max(even)
    even_minimum = min(even)

for i in range(0, len(odd)):
    if odd[i] > odd_maximum:
        odd_maximum = odd[i]
    elif odd[i] < odd_minimum:
        odd_minimum = odd[i]

for i in range(0, len(even)):
    if even[i] > even_maximum:
        even_maximum = even[i]
    elif even[i] < even_minimum:
        even_minimum = even[i]

print(f"OddSum={odd_sum:.2f},")
if mini == odd_minimum:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_minimum:.2f},")
if maxi == odd_maximum:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_maximum:.2f},")

print(f"EvenSum={even_sum:.2f},")
if mini == even_minimum:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_minimum:.2f},")
if maxi == even_maximum:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_maximum:.2f}")