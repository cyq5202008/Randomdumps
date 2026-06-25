def X(A):
    if A<=1:
        return False
    for i in range(2,A):
        if A % i ==0:
            return False
    else :
        return True
A = int(input("Masukan Nomor untuk cek prima atau tidak:"))

if X(A):
    print("True")
else:
    print("False")
