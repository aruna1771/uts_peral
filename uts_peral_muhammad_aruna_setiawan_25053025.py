menu = {
    "Kopi Susu": 18000,
    "Americano": 15000,
    "Cappuccino": 22000,
    "Matcha Latte": 25000,
    "Croissant": 12000,
    "Donat": 10000
}

voucher = 50000

daftar_menu = list(menu.items())

total_terbaik = 0
kombinasi_terbaik = []

for i in range(1, 2 ** len(daftar_menu)):

    kombinasi = []
    total = 0

    for j in range(len(daftar_menu)):

        if i & (1 << j):
            nama = daftar_menu[j][0]
            harga = daftar_menu[j][1]

            kombinasi.append(nama)
            total += harga
            
    if total <= voucher and total > total_terbaik:
        total_terbaik = total
        kombinasi_terbaik = kombinasi

print("================================")
print("       COFFEE SHOP VOUCHER")
print("================================")

print("Voucher tersedia : Rp", format(voucher, ","))
print("\nKombinasi menu terbaik:")

for item in kombinasi_terbaik:
    print("-", item, "Rp", format(menu[item], ","))

print("--------------------------------")
print("Total harga : Rp", format(total_terbaik, ","))
print("Sisa voucher: Rp", format(voucher - total_terbaik, ","))
print("================================")
