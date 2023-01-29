early_tax = int(input())

shoes_price = early_tax - early_tax * 0.4
suite_price = shoes_price - shoes_price * 0.2
ball_price = suite_price * 0.25
acessories_price = ball_price * 0.2

final_sum = early_tax + shoes_price + suite_price + ball_price + acessories_price

print(final_sum)