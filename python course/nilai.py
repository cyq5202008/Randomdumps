X =int(input("Welcome to Mark Converter! Please put your grade in:"))
def main(X):
    if X<60:
        return "You Got The Mark C"
    elif X<70:
        return "You Got The Mark B"
    elif X<80:
        return "You Got The Mark A"
    elif X<90:
        return "You Got The Mark A+"
    else:
        return "You Have Failed"
    
print(main(X))