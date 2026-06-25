import os
def load_data():
    data = {}
    with open('data.txt', 'r') as file:
        for line in file:
            nomorrekening, nama, saldo, pin = line.strip().split(',')
            data[nomorrekening] = {'nama': nama, 'saldo': int(saldo), 'pin': pin}
    return data

# Fungsi untuk menyimpan data ke file
def save_data(data):
    with open('data.txt', 'w') as file:
        for nomorrekening, info in data.items():
            file.write(f"{nomorrekening},{info['nama']},{info['saldo']},{info['pin']}\n")

# Fungsi registrasi pengguna baru
def registrasi(data):
    nomorrekening = input("Masukkan nomor rekening (6 angka): ")
    if nomorrekening in data:
        print("Nomor rekening sudah terdaftar!")
        return

    nama = input("Masukkan nama: ")
    saldo_awal = int(input("Masukkan saldo awal: "))
    pin = input("Masukkan PIN (4 angka): ")

    data[nomorrekening] = {'nama': nama, 'saldo': saldo_awal, 'pin': pin}
    save_data(data)
    print("Registrasi berhasil!")

# Fungsi login pengguna
def login(data):
    nomorrekening = input("Masukkan nomor rekening: ")
    pin = input("Masukkan PIN: ")

    if nomorrekening in data and data[nomorrekening]['pin'] == pin:
        print(f"Selamat datang, {data[nomorrekening]['nama']}!")
        return nomorrekening
    else:
        print("Nomor rekening atau PIN salah!")
        return None

# Fungsi penarikan tunai
def penarikan_tunai(data, nomorrekening):
    nominal = int(input("Masukkan nominal yang ingin diambil: "))
    if nominal > data[nomorrekening]['saldo']:
        print("Saldo anda tidak cukup!")
    else:
        data[nomorrekening]['saldo'] -= nominal
        save_data(data)
        print(f"Penarikan berhasil! Saldo Anda sekarang {data[nomorrekening]['saldo']}")

# Fungsi penyetoran tunai
def penyetoran_tunai(data, nomorrekening):
    nominal = int(input("Masukkan nominal yang ingin disetor: "))
    data[nomorrekening]['saldo'] += nominal
    save_data(data)
    print(f"Penyetoran berhasil! Saldo Anda sekarang {data[nomorrekening]['saldo']}")

# Fungsi pengecekan saldo
def check_saldo(data, nomorrekening):
    print(f"Saldo Anda: {data[nomorrekening]['saldo']}")

# Fungsi transfer dana
def transfer_dana(data, nomorrekening):
    rekening_tujuan = input("Masukkan nomor rekening tujuan: ")
    if rekening_tujuan not in data:
        print("Nomor rekening tujuan tidak ditemukan!")
        return

    nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
    if nominal > data[nomorrekening]['saldo']:
        print("Saldo anda tidak cukup!")
    else:
        data[nomorrekening]['saldo'] -= nominal
        data[rekening_tujuan]['saldo'] += nominal
        save_data(data)
        print("Transfer berhasil! Saldo Anda sekarang", {data[nomorrekening]['saldo']})

# Fungsi ganti PIN
def ganti_pin(data, nomorrekening):
    pin_lama = input("Masukkan PIN lama: ")
    if pin_lama != data[nomorrekening]['pin']:
        print("PIN lama salah!")
        return

    pin_baru = input("Masukkan PIN baru: ")
    if pin_baru == pin_lama:
        print("PIN baru tidak boleh sama dengan PIN lama!")
        return

    data[nomorrekening]['pin'] = pin_baru
    save_data(data)
    print("PIN berhasil diubah, silakan login kembali.")

# Menu utama setelah login
def menu_lanjutan(data, nomorrekening):
    while True:
        print("1. Penarikan Uang")
        print("2. Penyetoran Tunai")
        print("3. Check Saldo")
        print("4. Transfer Dana")
        print("5. Ganti PIN")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            penarikan_tunai(data, nomorrekening)
        elif pilihan == '2':
            penyetoran_tunai(data, nomorrekening)
        elif pilihan == '3':
            check_saldo(data, nomorrekening)
        elif pilihan == '4':
            transfer_dana(data, nomorrekening)
        elif pilihan == '5':
            ganti_pin(data, nomorrekening)
            break
        elif pilihan == '6':
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid!")

# Menu utama program
def menu_utama():
    data = load_data()
    while True:
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            nomorrekening = login(data)
            if nomorrekening:
                menu_lanjutan(data, nomorrekening)
        elif pilihan == '2':
            registrasi(data)
        elif pilihan == '3':
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()
