lenght = int(input()) / 10
width = int(input()) / 10
height = int(input()) / 10
percent = float(input()) / 100

all_volume_in_liters = lenght * width * height
final_volume = all_volume_in_liters - all_volume_in_liters * percent

print(final_volume)