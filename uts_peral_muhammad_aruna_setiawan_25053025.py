
import time

print("======================================")
print("       COFFEE SHOP VOUCHER SYSTEM")
print("======================================")

jumlah = int(input("Masukkan jumlah menu: "))

menu = []

for i in range(jumlah):
    print("\nMenu ke-", i + 1)

    nama = input("Nama menu  : ")
    harga = int(input("Harga (Rp) : "))

    menu.append({
        "nama": nama,
        "harga": harga
    })

voucher = int(input("\nMasukkan nominal voucher (Rp): "))

print("\n======================================")
print("          METODE BRUTE FORCE")
print("======================================")

mulai = time.perf_counter()

total_bf = 0
hasil_bf = []

for i in range(1, 2 ** jumlah):

    total = 0
    kombinasi = []

    for j in range(jumlah):

        if i & (1 << j):
            total += menu[j]["harga"]
            kombinasi.append(menu[j])

    if total <= voucher and total > total_bf:
        total_bf = total
        hasil_bf = kombinasi

waktu_bf = time.perf_counter() - mulai

print("Kombinasi terbaik:")

for item in hasil_bf:
    print("-", item["nama"], "Rp", format(item["harga"], ","))

print("Total : Rp", format(total_bf, ","))
print("Sisa  : Rp", format(voucher - total_bf, ","))
print("Waktu : {:.8f} detik".format(waktu_bf))


print("\n======================================")
print("             METODE GREEDY")
print("======================================")

mulai = time.perf_counter()

menu_urut = sorted(
    menu,
    key=lambda x: x["harga"],
    reverse=True
)

total_greedy = 0
hasil_greedy = []

for item in menu_urut:

    if total_greedy + item["harga"] <= voucher:

        hasil_greedy.append(item)
        total_greedy += item["harga"]

waktu_greedy = time.perf_counter() - mulai

# MENAMPILKAN HASIL GREEDY
print("Kombinasi terbaik:")

for item in hasil_greedy:
    print("-", item["nama"], "Rp", format(item["harga"], ","))

print("Total : Rp", format(total_greedy, ","))
print("Sisa  : Rp", format(voucher - total_greedy, ","))
print("Waktu : {:.8f} detik".format(waktu_greedy))

print("\n======================================")
print("         PERBANDINGAN METODE")
print("======================================")

print("Brute Force : Rp", format(total_bf, ","))
print("Greedy      : Rp", format(total_greedy, ","))

if total_bf > total_greedy:
    print("Hasil terbaik: BRUTE FORCE")

elif total_greedy > total_bf:
    print("Hasil terbaik: GREEDY")

else:
    print("Hasil terbaik: KEDUANYA SAMA")

print("\nWaktu Brute Force : {:.8f} detik".format(waktu_bf))
print("Waktu Greedy      : {:.8f} detik".format(waktu_greedy))

if waktu_bf < waktu_greedy:
    print("Lebih cepat: BRUTE FORCE")
elif waktu_greedy < waktu_bf:
    print("Lebih cepat: GREEDY")
else:
    print("Waktu eksekusi sama")

print("======================================")
