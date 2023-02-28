count_months = int(input())
electricity = []
water = 0
internet = 0
all_for_tok = 0

for i in range(0, count_months):
    electricity.append(float(input()))

for i in range(0, count_months):
    all_for_tok += electricity[i]
    water += 20
    internet += 15

others = (all_for_tok + water + internet) + (all_for_tok + water + internet) * 0.2
average = (all_for_tok + water + internet + others) / count_months

print(f"Electricity: {all_for_tok:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")
