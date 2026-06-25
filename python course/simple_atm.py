#Fitur-fitur di ATM ini : 
# 1. Load Accounts (Norek, Nama, Saldo, Pin) & Save Accounts
# 2. Register
# 3. Login
# 4. Check Saldo
# 5. Penarikan Uang (Withdraw)
# 6. Deposit (Penyetoran Tunai)
# 7. Transfer Dana
# 8. Ganti Pin

# Inovasi yang ditambahkan : 
# 1. Kemudahan dalam lalu lintas pembayaran internasional 
# 2. Penyediaan mata uang asing (Check Balance, withdraw, dan transfer)

import os

a = 16400 #usd
b = 12185 #sgd
c = 10884 #aud
d = 3476 #myr
e = 447 #thb
f = 104 #jpy
g = 2260 #cny
h = 11.93 #krw
i = 4393 #sar
j = 17673 #eur
k = 20917 #gbp
l = 197 #inr
m = 502 #try

DATA_FILE = 'data.txt'
def load_accounts():
    accounts = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            for line in file:
                nomor_rekening, nama, saldo, pin = line.strip().split(',')
                accounts[nomor_rekening] = {
                    'nama': nama,
                    'saldo': int(saldo),
                    'pin': pin
                }
    return accounts

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        for nomor_rekening, info in accounts.items():
            file.write(f"{nomor_rekening},{info['nama']},{info['saldo']},{info['pin']}\n")

def register():
    accounts = load_accounts()
    nomor_rekening = input("Masukkan nomor rekening baru (6 digit): ")
    if nomor_rekening in accounts:
        print("Nomor rekening sudah ada.")
        return
    nama = input("Masukkan nama Anda: ")
    saldo = int(input("Masukkan saldo awal: "))
    pin = input("Masukkan PIN 4 digit: ")
    accounts[nomor_rekening] = {
        'nama': nama,
        'saldo': saldo,
        'pin': pin
    }
    save_accounts(accounts)
    print("Registrasi berhasil!")

def login():
    accounts = load_accounts()
    nomor_rekening = input("Masukkan nomor rekening Anda: ")
    pin = input("Masukkan PIN Anda: ")
    if nomor_rekening in accounts and accounts[nomor_rekening]['pin'] == pin:
        print("Login berhasil!")
        return nomor_rekening
    else:
        print("Nomor rekening atau PIN salah.")
        return None

def check_balance(nomor_rekening):
    accounts = load_accounts()
    print(f"Saldo Anda dalam Rupiah adalah: {accounts[nomor_rekening]['saldo']}")
    print()
    print("Cek Saldo Dalam: ")
    print(f"1. United States Dollar")
    print(f"2. Singapore Dollar")
    print(f"3. Australian Dollar")
    print(f"4. Malaysian Ringgit")
    print(f"5. Thai Baht")
    print(f"6. Japanese Yen")
    print(f"7. Chinese Yuan")
    print(f"8. South Korean Won")
    print(f"9. Saudi Arabian Riyal")
    print(f"10. Euro")
    print(f"11. Great Britain Pound")
    print(f"12. Indian Rupee")
    print(f"13. Turkish Lira")
    print(f"14. Keluar")
    curr_choice = input('Pilih opsi : ')
    if curr_choice == '1':
        print(f"Saldo : USD {accounts[nomor_rekening]['saldo']/a}")
        return
    elif curr_choice == '2':
        print(f"Saldo: SGD {accounts[nomor_rekening]['saldo']/b}")
        return
    elif curr_choice == '3':
        print(f"Saldo: AUD {accounts[nomor_rekening]['saldo']/c}")
        return
    elif curr_choice == '4':
        print(f"Saldo: MYR {accounts[nomor_rekening]['saldo']/d}")
        return
    elif curr_choice == '5':
        print(f"Saldo: THB {accounts[nomor_rekening]['saldo']/e}")
        return
    elif curr_choice == '6':
        print(f"Saldo: JPY {accounts[nomor_rekening]['saldo']/f}")
        return
    elif curr_choice == '7':
        print(f"Saldo: CNY {accounts[nomor_rekening]['saldo']/g}")
        return
    elif curr_choice == '8':
        print(f"Saldo: KRW {accounts[nomor_rekening]['saldo']/h}")
        return
    elif curr_choice == '9':
        print(f"Saldo: SAR {accounts[nomor_rekening]['saldo']/i}")
        return
    elif curr_choice == '10':
        print(f"Saldo: EUR {accounts[nomor_rekening]['saldo']/j}")
        return
    elif curr_choice == '11':
        print(f"Saldo: GBP {accounts[nomor_rekening]['saldo']/k}")
        return
    elif curr_choice == '12':
        print(f"Saldo: INR {accounts[nomor_rekening]['saldo']/l}")
        return
    elif curr_choice == '13':
        print(f"Saldo: TRY {accounts[nomor_rekening]['saldo']/m}")
        return
    elif curr_choice == '14':
        print("Cancelled")
    else:
        print("System Error")


def withdraw(nomor_rekening):
    accounts = load_accounts()
    print("Pilih mata uang :")
    print(f"1. Indonesian Rupiah")
    print(f"2. United States Dollar")
    print(f"3. Singapore Dollar")
    print(f"4. Australian Dollar")
    print(f"5. Malaysian Ringgit")
    print(f"6. Thai Baht")
    print(f"7. Japanese Yen")
    print(f"8. Chinese Yuan")
    print(f"9. South Korean Won")
    print(f"10. Saudi Arabian Riyal")
    print(f"11. Euro")
    print(f"12. Great Britain Pound")
    print(f"13. Indian Rupee")
    print(f"14. Turkish Lira")
    choices = input('Pilih opsi : ')
    amount = int(input("Masukkan jumlah uang yang ingin ditarik (Tulis dalam Rupiah terlebih dahulu): "))
    if amount > accounts[nomor_rekening]['saldo']:
        print("Saldo Anda tidak cukup.")
    else:
        accounts[nomor_rekening]['saldo'] -= amount
        save_accounts(accounts)
        if choices == '1':
            print("Penarikan berhasil sebesar Rp", amount)
            print("Saldo saat ini sebesar : Rp", {accounts[nomor_rekening]['saldo']})
        elif choices == '2':
            print("Penarikan berhasil sebesar USD", amount/a)
            print("Saldo saat ini sebesar : USD", {accounts[nomor_rekening]['saldo']/a})
        elif choices == '3':
            print("Penarikan berhasil sebesar SGD", amount/b)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/b})
        elif choices == '4':
            print("Penarikan berhasil sebesar AUD", amount/c)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/c})
        elif choices == '5':
            print("Penarikan berhasil sebesar MYR", amount/d)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/d})
        elif choices == '6':
            print("Penarikan berhasil sebesar THB", amount/e)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/e})
        elif choices == '7':
            print("Penarikan berhasil sebesar JPY", amount/f)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/f})
        elif choices == '8':
            print("Penarikan berhasil sebesar CNY", amount/g)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/g})
        elif choices == '9':
            print("Penarikan berhasil sebesar KRW", amount/h)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/h})
        elif choices == '10':
            print("Penarikan berhasil sebesar SAR", amount/i)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/i})
        elif choices == '11':
            print("Penarikan berhasil sebesar EUR", amount/j)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/j})
        elif choices == '12':
            print("Penarikan berhasil sebesar GBP", amount/k)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/k})
        elif choices == '13':
            print("Penarikan berhasil sebesar INR", amount/l)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/l})
        elif choices == '14':
            print("Penarikan berhasil sebesar TRY", amount/m)
            print("Saldo saat ini sebesar : AUD", {accounts[nomor_rekening]['saldo']/m})
        else:
            print("Penarikan tunai gagal")

def deposit(nomor_rekening):
    accounts = load_accounts()
    amount = int(input("Masukkan jumlah uang yang ingin disetor: "))
    accounts[nomor_rekening]['saldo'] += amount
    save_accounts(accounts)
    print("Penyetoran berhasil!")

def transfer(nomor_rekening):
    accounts = load_accounts()
    target_account = input("Masukkan nomor rekening tujuan: ")
    if target_account not in accounts:
        print("Nomor rekening tujuan tidak ada.")
        return
    print("Pilih mata uang :")
    print(f"1. Indonesian Rupiah")
    print(f"2. United States Dollar")
    print(f"3. Singapore Dollar")
    print(f"4. Australian Dollar")
    print(f"5. Malaysian Ringgit")
    print(f"6. Thai Baht")
    print(f"7. Japanese Yen")
    print(f"8. Chinese Yuan")
    print(f"9. South Korean Won")
    print(f"10. Saudi Arabian Riyal")
    print(f"11. Euro")
    print(f"12. Great Britain Pound")
    print(f"13. Indian Rupee")
    print(f"14. Turkish Lira")
    choices = input('Pilih opsi : ')
    amount = int(input("Masukkan jumlah yang ingin ditransfer (Tulis dalam Rupiah terlebih dahulu): "))
    if amount > accounts[nomor_rekening]['saldo']:
        print("Saldo Anda tidak cukup.")
    else:
        accounts[nomor_rekening]['saldo'] -= amount
        accounts[target_account]['saldo'] += amount
        save_accounts(accounts)
        if choices == '1':
            print("Transfer berhasil sebesar Rp", amount)
            print("Saldo saat ini sebesar : Rp", {accounts[nomor_rekening]['saldo']})
        elif choices == '2':
            print("Transfer berhasil sebesar USD", amount/a)
            print("Saldo saat ini sebesar : Rp", {accounts[nomor_rekening]['saldo']/a})
        elif choices == '3':
            print("Transfer berhasil sebesar SGD", amount/b)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/b})
        elif choices == '4':
            print("Transfer berhasil sebesar AUD", amount/c)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/c})
        elif choices == '5':
            print("Transfer berhasil sebesar MYR", amount/d)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/d})
        elif choices == '6':
            print("Transfer berhasil sebesar THB", amount/e)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/e})
        elif choices == '7':
            print("Transfer berhasil sebesar JPY", amount/f)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/f})
        elif choices == '8':
            print("Transfer berhasil sebesar CNY", amount/g)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/g})
        elif choices == '9':
            print("Transfer berhasil sebesar KRW", amount/h)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/h})
        elif choices == '10':
            print("Transfer berhasil sebesar SAR", amount/i)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/i})
        elif choices == '11':
            print("Transfer berhasil sebesar EUR", amount/j)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/j})
        elif choices == '12':
            print("Transfer berhasil sebesar GBP", amount/k)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/k})
        elif choices == '13':
            print("Transfer berhasil sebesar INR", amount/l)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/l})
        elif choices == '14':
            print("Transfer berhasil sebesar TRY", amount/m)
            print("Saldo saat ini sebesar : SGD", {accounts[nomor_rekening]['saldo']/m})
        else:
            print("Transfer tunai gagal")

def kurs(nomor_rekening):
    import datetime
    current_time = datetime.datetime.now()
    print(current_time)
    print("1. 1 USD = Rp", a)
    print("2. 1 SGD = Rp", b)
    print("3. 1 AUD = Rp", c)
    print("4. 1 MYR = Rp", d)
    print("5. 1 THB = Rp", e)
    print("6. 1 JPY = Rp", f)
    print("7. 1 CNY = Rp", g)
    print("8. 1 KRW = Rp", h)
    print("9. 1 SAR = Rp", i)
    print("10. 1 EUR = Rp", j)
    print("11. 1 GBP = Rp", k)
    print("12. 1 INR = Rp", l)
    print("13. 1 TRY = Rp", m)

def change_pin(nomor_rekening):
    accounts = load_accounts()
    old_pin = input("Masukkan PIN saat ini: ")
    if accounts[nomor_rekening]['pin'] != old_pin:
        print("PIN salah.")
        return
    new_pin = input("Masukkan PIN baru 4 digit: ")
    if new_pin == old_pin:
        print("PIN baru tidak boleh sama dengan PIN lama.")
        return
    accounts[nomor_rekening]['pin'] = new_pin
    save_accounts(accounts)
    print("PIN berhasil diganti!")

def main():
    while True:
        print()
        print("================= SELAMAT DATANG DI LAYANAN ATM BANK SALMAN =================")
        print()
        print("Silahkan memilih pilihan berikut : ")
        print("\n1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        print()
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            nomor_rekening = login()
            if nomor_rekening:
                while True:
                    print("\n1. Penarikan Uang")
                    print("2. Penyetoran Tunai")
                    print("3. Check Saldo")
                    print("4. Transfer Dana")
                    print("5. Ganti PIN")
                    print("6. Lihat kurs saat ini")
                    print("7. Keluar")
                    sub_choice = input("Pilih opsi: ")
                    print()
                    if sub_choice == '1':
                        withdraw(nomor_rekening)
                    elif sub_choice == '2':
                        deposit(nomor_rekening)
                    elif sub_choice == '3':
                        check_balance(nomor_rekening)
                    elif sub_choice == '4':
                        transfer(nomor_rekening)
                    elif sub_choice == '5':
                        change_pin(nomor_rekening)
                        break
                    elif sub_choice == '6':
                        kurs(nomor_rekening)
                    elif sub_choice == '7':
                        break
                    else:
                        print("Opsi tidak valid. Silakan coba lagi.")
        elif choice == '3':
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()