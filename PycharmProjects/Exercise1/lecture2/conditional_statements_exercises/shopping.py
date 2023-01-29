budget = float(input())
count_videocarts = int(input())
count_processors = int(input())
count_ram_memory = int(input())

videocart = 250.0
price_videocarts = videocart * count_videocarts

processor = price_videocarts * 0.35
price_processors = processor * count_processors

ram_memory = price_videocarts * 0.1
price_ram_memory = ram_memory * count_ram_memory

total_price = price_processors + price_ram_memory + price_videocarts

if count_videocarts > count_processors:
    total_price = total_price - total_price * 0.15

if total_price <= budget:
    left_money = budget - total_price
    print(f'You have {left_money:.2f} leva left!')
else:
    needed_money = total_price - budget
    print(f'Not enough money! You need {needed_money:.2f} leva more!')