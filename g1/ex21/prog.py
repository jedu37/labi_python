f = open("g1/ex21/file.txt","r")

rev = ""
nLine = ""

for line in f:
    if line =="":
        break

    s = line.split()
    nLine = ""
    for word in s:
        rev = ""
        for c in word:
            rev = c + rev
        nLine = nLine + ' ' + rev
        
    print(nLine + "\n")