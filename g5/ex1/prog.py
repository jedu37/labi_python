import csv
import sys

def main(argv):
    info = []
    fich_csv = open(argv[1], "r")

    reader = csv.DictReader(fich_csv, delimiter=',')

    for row in reader:
        info.append(row)
    fich_csv.close()

    minimo = sys.float_info.max
    maximo = sys.float_info.min
    soma = 0

    for i in info:
        t = float(i['value'])
        
        if t > maximo:
            maximo = t

        if t < minimo:
            minimo = t

        soma += t

    print("Temperatura Máxima: %4.2f\nTemperatura Mínima: %4.2f\nTemperatura Média: %4.2f"%(maximo,minimo,(soma/len(info))))


main(sys.argv)
