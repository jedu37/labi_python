s = input("Frase? ->")

c = 0

n = s.split()

for i in n:
    if i.isalpha:
        c += 1

print("A frase tem %d palavras"%(c))