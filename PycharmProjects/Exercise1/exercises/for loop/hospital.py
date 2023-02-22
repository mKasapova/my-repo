days = int(input())
docs = 7
treated_patiens = 0
untreated_patiens = 0
count_patients = []
for i in range(0, days):
    count_patients.insert(i, int(input()))

for i in range(0, days):
    if (i+1) % 3 == 0 and untreated_patiens > treated_patiens:
        docs += 1
    if count_patients[i] <= docs:
        treated_patiens += count_patients[i]
    else:
        treated_patiens += docs
        untreated_patiens += count_patients[i] - docs

print(f"Treated patients: {treated_patiens}.")
print(f"Untreated patients: {untreated_patiens}.")






