def traduzir(frase):
    frase = frase.replace("r","")
    frase = frase.replace("l","u")
    frase = frase.replace("R","")
    frase = frase.replace("L","U")

    return frase

def main():
    while True:
        n = input("Frase->")
        
        if n == "":
            break

        print("->"+traduzir(n))

if __name__ == "__main__":
    main()
