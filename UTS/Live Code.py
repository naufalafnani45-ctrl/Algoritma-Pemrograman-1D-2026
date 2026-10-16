tiket = 3
reguler = 40000
vip = 75000
vvip = 100000

while True:
    beli_tiket = int(input("masukkan tiket yang dibeli:"))
    beli_tiket =+ 1
    if beli_tiket > 1:
        harga_tiket = vip + vvip
        harga_tiket =+ beli_tiket
        print("tiket udah lebih dari ketentuan")
        print(harga_tiket)
        continue


if reguler == 40000:
    tambahan_minuman = input("masukkan Y/N:")
    harga_minuman = 10000
    if tambahan_minuman == Y:
        print("akan mendapat tawaran minuman seharga Rp. 10000")
    else :
        print("pilihan N tidak dapat tawaran")

if beli_tiket > 3:
    ada_member_card = beli_tiket * 0.15
    tidak_member_card = beli_tiket * 0.10
    print("ada member card:", ada_member_card)
    print("tidak ada member card:", tidak_member_card)

while True:
    pembayaran = int(input("uang yang di bayar: Rp"))
    harga_tiket = harga_tiket - pembayaran
    print(harga_tiket)


