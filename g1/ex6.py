l = []
l1 = []
l2 = []

l1.append('Homem')
l1.append('Leão')
l1.append('Mulher')

l2.append("peixe")
l2.append("borboleta")
l2.append("slug")

print("Comprimento de l1 -> %d"%(len(l1)))
print("Comprimento de l2 -> %d"%(len(l2)))

l.extend(l1)
l.extend(l2)

print(l[1:3])

print(l)
print(len(l))