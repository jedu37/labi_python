import os.path
import sys

fname = "g1/ex22/file.txt"

if not os.path.exists(fname):
    sys.exit("Não existe")

if os.path.isdir(fname):
    sys.exit("É diretório")

if not os.path.isfile(fname):
    sys.exit("Não é ficheiro")
    
f = open(fname,"r")

rev = ""
revLine = ""
nline = 0
nWord = 0
nChar = 0

for line in f:
    if line =="":
        break
    
    nline += 1

    s = line.split()
    revLine = ""

    for word in s:
        nWord += 1
        nChar += len(word)

        rev = ""
        for c in word:
            rev = c + rev
        revLine = revLine + ' ' + rev
        
    print(revLine + "\n")


print("O ficheiro tem %d linhas, %d palavras e %d caracteres"%(nline,nWord,nChar))