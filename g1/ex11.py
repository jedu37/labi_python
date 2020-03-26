# encoding=utf-8

ano = int(input("Ano ? -> "))

if ano%4 == 0 & ano%400 == 0:
    print('Ano bissexto')
else:
    print('Ano não bissexto')