def primo(n):
    cond = True
    for i in range(0,n):
        if i > 1:
            if(n%i==0):
                cond=False
                break
    
    return cond

def main():
    while True:
        c = int(input("Número Primo->"))
        if c == 0:
            break
        print(primo(c))
    

if __name__ == "__main__":
    main()