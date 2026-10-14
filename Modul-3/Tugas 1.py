jumlah = 0            # banyak penumpang
total = 0             # total jarak
terjauh = 0          # jarak terjauh
total_jarak = 0     # Penjumlahan semua jarak
tarif = 0             # tarif per penumpang

while True:
    jarak = int(input("Masukkan Jarak(0 = Selesai)"))
    if jarak == 0:
        break
    if jarak > 0:
        if jarak > terjauh:
            terjauh = jarak
    else :
        continue


    jumlah = jumlah + 1
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah % 5 == 0:
        tarif = tarif * 0.5

    print("Tarif:", tarif)
    total = tarif + tarif
    total_jarak = total_jarak + jarak

print("Jumlah penumpang", jumlah)
print("total pendapatan", total)
print("Jarak terjauh:", terjauh, "km")
if jumlah > 0:
    print("Rata-rata Jarak:", total_jarak / jumlah)
else:
    print("Rata Rata Jarak: 0km")
