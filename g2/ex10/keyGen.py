import sys,os
from Crypto.PublicKey import RSA

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
    
    bits = int(sys.argv[2])

    keypair = RSA.generate(bits)

    fout = open(fname,"wb")

    kp = keypair.exportKey("PEM","letmein")

    fout.write(kp)

    fout.close()

if __name__ == "__main__":
    main()