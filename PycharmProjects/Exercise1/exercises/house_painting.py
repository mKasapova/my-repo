x = float(input())
y = float(input())
h = float(input())

razhod_zelena_boya = 3.4
razhod_chervena_boya = 4.3

vrata = 1.2 * 2
prozorec = 1.5 * 1.5
zadna_stena = x * x
predna_stena = (x * x) - vrata
stranichna_stena = (x * y) - prozorec

plosht_steni = predna_stena + zadna_stena + 2 * stranichna_stena

pokriv_pravoygalnik = x * y
pokriv_triygalnik = (x * h) / 2

plosht_pokriv = 2 * (pokriv_pravoygalnik + pokriv_triygalnik)

litri_zelena_boq = plosht_steni / razhod_zelena_boya
litri_chervena_boq = plosht_pokriv / razhod_chervena_boya

print(f"{litri_zelena_boq:.2f}")
print(f"{litri_chervena_boq:.2f}")