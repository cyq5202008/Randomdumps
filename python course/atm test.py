import os

# Fungsi untuk memuat data dari file
def load_data():
    data = {}
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as file:
            for line in file:
                nomor_rekening, nama, saldo, pin = line.strip().split(',')
                data[nomor_rekening] = {'nama': nama, 'saldo': int(saldo), 'pin': pin}
    return data

# Fungsi untuk menyimpan data ke file
def save_data(data):
    with open('data.txt', 'w') as file:
        for nomor_rekening, info in data.items():
            file.write(f"{nomor_rekening},{info['nama']},{info['saldo']},{info['pin']}\n")

# Fungsi registrasi pengguna baru
def registrasi(data):
    nomor_rekening = input("Masukkan nomor rekening (6 angka): ")
    if nomor_rekening in data:
        print("Nomor rekening sudah terdaftar!")
        return

    nama = input("Masukkan nama: ")
    saldo_awal = int(input("Masukkan saldo awal: "))
    pin = input("Masukkan PIN (4 angka): ")

    data[nomor_rekening] = {'nama': nama, 'saldo': saldo_awal, 'pin': pin}
    save_data(data)
    print("Registrasi berhasil!")

# Fungsi login pengguna
def login(data):
    nomor_rekening = input("Masukkan nomor rekening: ")
    pin = input("Masukkan PIN: ")

    if nomor_rekening in data and data[nomor_rekening]['pin'] == pin:
        print(f"Selamat datang, {data[nomor_rekening]['nama']}!")
        return nomor_rekening
    else:
        print("Nomor rekening atau PIN salah!")
        return None

# Fungsi penarikan tunai
def penarikan_tunai(data, nomor_rekening):
    nominal = int(input("Masukkan nominal yang ingin diambil: "))
    if nominal > data[nomor_rekening]['saldo']:
        print("Saldo anda tidak cukup!")
    else:
        data[nomor_rekening]['saldo'] -= nominal
        save_data(data)
        print(f"Penarikan berhasil! Saldo Anda sekarang {data[nomor_rekening]['saldo']}")

# Fungsi penyetoran tunai
def penyetoran_tunai(data, nomor_rekening):
    nominal = int(input("Masukkan nominal yang ingin disetor: "))
    data[nomor_rekening]['saldo'] += nominal
    save_data(data)
    print(f"Penyetoran berhasil! Saldo Anda sekarang {data[nomor_rekening]['saldo']}")

# Fungsi pengecekan saldo
def check_saldo(data, nomor_rekening):
    print(f"Saldo Anda: {data[nomor_rekening]['saldo']}")

# Fungsi transfer dana
def transfer_dana(data, nomor_rekening):
    rekening_tujuan = input("Masukkan nomor rekening tujuan: ")
    if rekening_tujuan not in data:
        print("Nomor rekening tujuan tidak ditemukan!")
        return

    nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
    if nominal > data[nomor_rekening]['saldo']:
        print("Saldo anda tidak cukup!")
    else:
        data[nomor_rekening]['saldo'] -= nominal
        data[rekening_tujuan]['saldo'] += nominal
        save_data(data)
        print(f"Transfer berhasil! Saldo Anda sekarang {data[nomor_rekening]['saldo']}")

# Fungsi ganti PIN
def ganti_pin(data, nomor_rekening):
    pin_lama = input("Masukkan PIN lama: ")
    if pin_lama != data[nomor_rekening]['pin']:
        print("PIN lama salah!")
        return

    pin_baru = input("Masukkan PIN baru: ")
    if pin_baru == pin_lama:
        print("PIN baru tidak boleh sama dengan PIN lama!")
        return

    data[nomor_rekening]['pin'] = pin_baru
    save_data(data)
    print("PIN berhasil diubah, silakan login kembali.")

# Menu utama setelah login
def menu_lanjutan(data, nomor_rekening):
    while True:
        print("\n1. Penarikan Uang")
        print("\n2. Penyetoran Tunai")
        print("\n3. Check Saldo")
        print("\n4. Transfer Dana")
        print("\n5. Ganti PIN")
        print("\n6. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            penarikan_tunai(data, nomor_rekening)
        elif pilihan == '2':
            penyetoran_tunai(data, nomor_rekening)
        elif pilihan == '3':
            check_saldo(data, nomor_rekening)
        elif pilihan == '4':
            transfer_dana(data, nomor_rekening)
        elif pilihan == '5':
            ganti_pin(data, nomor_rekening)
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
        print("\n1. Login")
        print("\n2. Registrasi")
        print("\n3. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            nomor_rekening = login(data)
            if nomor_rekening:
                menu_lanjutan(data, nomor_rekening)
        elif pilihan == '2':
            registrasi(data)
        elif pilihan == '3':
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()
