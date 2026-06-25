A =int(input("Input A:"))
B =int(input("Input B:"))
C =int(input("Input C:"))
if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B) 
else:
    print(C)