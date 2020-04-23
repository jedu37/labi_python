import sys, os.path
from Crypto.Hash import SHA256

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
    
    g = open(fname,"r")

    d = SHA256.new()

    for line in g:
        d.update(line.encode("utf-8"))
    
    g.close()

    print(d.hexdigest())

    f = open(fname,"rb")
    buffer = f.read(512)

    h = SHA256.new()

    while len(buffer) > 0:
        h.update(buffer)
        buffer = f.read(512)
    
    f.close()

    print(h.hexdigest())

if __name__ == "__main__":
    main()