import os,sys,string
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

def isHex(s):
    hex_digits = set(string.hexdigits)
    return all(c in hex_digits for c in s)

def main():
    if len(sys.argv) < 3:
        sys.exit("Not Enough Arguments")
    
    fname = sys.argv[1]

    if not os.path.exists(fname):
        sys.exit("Não existe")

    if os.path.isdir(fname):
        sys.exit("É diretório")

    if not os.path.isfile(fname):
        sys.exit("Não é ficheiro")

    key = sys.argv[2]

    if not(isHex(key) and len(key) >= 5 and len(key) <= 256):
        if len(key) > 256:
            key = key[0:255]
        else:
            h = SHA.new()
            h.update(key.encode("utf-8"))
            key = h.hexdigest()[0:31]
    
    f = open(fname,"r")
    content = f.read()
    f.close()
    cipher = ARC4.new(key)
    cryptogram = cipher.encrypt(content.encode("utf-8"))
    os.write(1, cryptogram)


if __name__ == "__main__":
    main()
