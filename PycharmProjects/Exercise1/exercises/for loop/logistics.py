count_cargos = int(input())
all_cargos = 0
tons_microbus = 0
tons_truck = 0
tons_train = 0
tons_cargo = []

for i in range(0, count_cargos):
    tons_cargo.insert(i, int(input()))

for i in range(0, len(tons_cargo)):
    all_cargos += tons_cargo[i]
    if tons_cargo[i] <= 3:
        tons_microbus += tons_cargo[i]
    elif 4 <= tons_cargo[i] <= 11:
        tons_truck += tons_cargo[i]
    else:
        tons_train += tons_cargo[i]

average_tons = (tons_microbus * 200 + tons_truck * 175 + tons_train * 120) / all_cargos
microbus_percent = (tons_microbus / all_cargos) * 100
truck_percent = (tons_truck / all_cargos) * 100
train_percent = (tons_train / all_cargos) * 100

print(f"{average_tons:.2f}")
print(f"{microbus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")