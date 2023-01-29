deposit = float(input())
deposit_limit = int(input())
early_percent = float(input()) / 100

sum_deposit = deposit + deposit_limit * ((deposit * early_percent) / 12)

print(sum_deposit)
