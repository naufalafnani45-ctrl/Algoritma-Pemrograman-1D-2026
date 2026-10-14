n = int(input("tinggi setengah menatar (2-15)"))
while n < 2 or n > 15:
    print("tidak valid, masukkan angka 2-15")
    n = int(input("tinggi setengah menara (2-15)"))

lebar = 2 * n - 1
baris_list = list(range(1, n + 1)) + list(range(n - 1, 0, -1))

list = list(5,6,7,8)

for i in baris_list:
    s = ""
    for k in range(1, i + 1):
        s = s + str(k % 10)
    for k in range(i - 1, 0, -1):
        s = s + str(k % 10)
    print(s.center(lebar))
