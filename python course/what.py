X = int(input("Uang Pertama Kevin:"))
Y = int(input("Harga Barang:"))
Z = int(input("Diskon:"))

def Hitung(X,Y,Z):
    if X<(Y*((100-Z)/100)):
        return "Kevin tidak jadi membeli barang karena terlalu mahal."
    sisa_uang = (X-(Y*((100-Z)/100)))
    return f"Kevin membawa uang {X} dan membeli barang dengan harga {Y}, ternyata barang tersebut mendapat diskon sebesar {Z}% presen. Sisa uang Kevin adalah {sisa_uang}"

hasil = Hitung(X, Y, Z)
print(hasil)
