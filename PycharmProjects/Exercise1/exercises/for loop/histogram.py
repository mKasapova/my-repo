n = int(input())
counter_p1 = 0
counter_p2 = 0
counter_p3 = 0
counter_p4 = 0
counter_p5 = 0

for i in range(0, n):
    num = int(input())
    if num < 200:
        counter_p1 += 1
    elif 200 <= num <= 399:
        counter_p2 += 1
    elif 400 <= num <= 599:
        counter_p3 += 1
    elif 600 <= num <= 799:
        counter_p4 +=1
    elif 800 <= num:
        counter_p5 += 1

p1 = counter_p1 / n * 100
p2 = counter_p2 / n * 100
p3 = counter_p3 / n * 100
p4 = counter_p4 / n * 100
p5 = counter_p5 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")