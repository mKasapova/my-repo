w_in_m = float(input())
h_in_m = float(input())

w_in_cm = w_in_m * 100
h_in_cm = h_in_m * 100

h_without_coridor = h_in_cm - 100
count_desk_in_row = h_without_coridor // 70
count_rows = w_in_cm // 120

count_places = count_desk_in_row * count_rows - 3

print(count_places)