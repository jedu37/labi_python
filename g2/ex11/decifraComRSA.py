import os,sys,string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def main():
    if len(sys.argv) < 3:
        sys.exit("Not Enough Arguments")
    
    keyf = sys.argv[1]

    if not os.path.exists(keyf):
        sys.exit("Não existe")

    if os.path.isdir(keyf):
        sys.exit("É diretório")

    if not os.path.isfile(keyf):
        sys.exit("Não é ficheiro")

    fname = sys.argv[2]

    if not os.path.exists(fname):
        sys.exit("Não existe")

    if os.path.isdir(fname):
        sys.exit("É diretório")

    if not os.path.isfile(fname):
        sys.exit("Não é ficheiro")
    
    k = open(keyf,"r")
    keypair = RSA.importKey(k.read(),"letmein")
    cipher = PKCS1_OAEP.new(keypair)

    f = open(fname,"r")

    print(cipher.decrypt(f.read()).decode('utf-8'))

    f.close()


if __name__ == "__main__":
    main()