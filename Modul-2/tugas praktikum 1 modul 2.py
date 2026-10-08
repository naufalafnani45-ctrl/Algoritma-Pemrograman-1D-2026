password = int(input("masukkan tiga digit password:"))

digit1 = password // 100
digit2 = (password // 10) % 10
digit3 = password % 10

pelacak_awal = digit1 * digit3

if digit2 % 2 == 1 :
    pelacak1 = pelacak_awal + 25
else :
    pelacak1 = pelacak_awal - digit2

if pelacak1 % 3 == 0 : 
    pelacak2 = pelacak1 // 3
else :
    pelacak2 = pelacak1 * 2

if pelacak2 > 50 :
    status = "kategori A"
elif pelacak2 > 20 :
    status = "kategori B"
else :
    status = "password di tolak"

if pelacak2 % 2 == 0 :
    siklus = "siklus genap"
else :
    siklus = "siklus ganjil"

print("===HASIL PASSWORD===")
print("Digit Pertama: ", int(digit1))
print("digit kedua: ", int(digit2))
print("digit ketiga:", int(digit3))
print("Pelacak 1: ", int(pelacak1))
print("Pelacak 2: ", int(pelacak2))
print("Status: ", status)
print("Siklus: ", siklus)
