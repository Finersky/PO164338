def main():
    #a
    lista1 = []
    for x in range(11):
        if x != 0:
            lista1.append(x)
    print(lista1)
    # b
    lista2 = []
    for x in range(11):
        if x != 0:
            lista2.append(x * 2)
    print(lista2)
    # c
    lista3 = []
    for x in range(11):
        if x != 0:
            lista3.append(x * x)
    print(lista3)
    # d
    lista4 = []
    for x in range(11):
        if x != 0:
            lista4.append(0)
    print(lista4)
    # e
    lista5 = []
    for x in range(11):
        if x % 2 == 0:
            lista5.append(0)
        else:
            lista5.append(1)
    print(lista5)
    #f - NIEGOTOWE
    lista6 = []
    for x in range(11):
        if x%5 == 0:
            lista6.append(x)

    print(lista6)
