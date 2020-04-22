import hashlib, sys, os.path

def main():
    if len(sys.argv) < 2:
        sys.exit("Not Enough Arguments")
    
    fname = sys.argv[1]

    if not os.path.exists(fname):
        sys.exit("Não existe")

    if os.path.isdir(fname):
        sys.exit("É diretório")

    if not os.path.isfile(fname):
        sys.exit("Não é ficheiro")

    f = open(fname,"r")

    h = hashlib.sha1()

    for line in f:
        h.update(line.encode("utf-8"))
    
    print(h.hexdigest())

if __name__ == "__main__":
    main()