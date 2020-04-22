def mul3(a,b):
    c = 0

    for i in range(a,b):
        if i%3==0:
            c +=1
    
    return c


def main():
    print("insira 2 valores")
    x = int(input("->"))
    y = int(input("->"))

    print("entre %d e %d, existem %d múltiplos de 3"%(x,y,mul3(x,y)))

if __name__ == "__main__":
    main()