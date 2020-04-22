import random

def init(a,b):
    return random.randint(a,b)  

def guess(n):
    g = int(input("Tentativa->"))

    if g == n:
        return True
    elif g < n:
        print("Maior")
        return False
    elif g > n:
        print("Menor")
        return False

def main():
    trys = 0

    n = init(0,100)

    while True:
        trys += 1
        if guess(n):
            break
    
    print("Nº Tentativas: %d"%(trys))


if __name__ == "__main__":
    main()