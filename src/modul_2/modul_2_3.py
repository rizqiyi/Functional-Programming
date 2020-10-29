# Kegiatan 3
result = []


def inputValues(rows, columns):
    for i in range(rows):
        a = []
        for j in range(columns):
            a.append(int(input(f'[{i}][{j}] : ')))
        result.append(a)
    return tuple(result)


def square(val):
    a = []
    for x in range(0, len(val)):
        b = []
        for z in range(0, len(val[x])):
            square = val[x][z] * val[x][z]
            b.append(square)
        a.append(b)
    return tuple(a)


def addition(val):
    a = []
    for x in range(0, len(val)):
        b = []
        for z in range(0, len(val[x])):
            resultAdd = val[x][z] + val[x][z]
            b.append(resultAdd)
        a.append(b)
    return tuple(a)


def reduction(val):
    a = []
    for x in range(0, len(val)):
        b = []
        for z in range(0, len(val[x])):
            resultReduction = val[x - 1][z - 1] - val[x][z]
            b.append(resultReduction)
        a.append(b)
    return tuple(a)


def multiply(val):
    a = []
    for x in range(0, len(val)):
        b = []
        for z in range(0, len(val[x])):
            resultMult = val[x - 1][z - 1] * val[x][z]
            b.append(resultMult)
        a.append(b)
    return tuple(a)


def division(val):
    a = []
    for x in range(0, len(val)):
        b = []
        for z in range(0, len(val[x])):
            resultDiv = val[x - 1][z - 1] / val[x][z]
            b.append(round(resultDiv, 2))
        a.append(b)
    return tuple(a)


rows = int(input("Masukkan jumlah baris : "))
columns = int(input("Masukkan jumlah kolom : "))
print("Masukkan nilai : ")
print(f'\nInput : {inputValues(rows, columns)}\n')

print(f'Kuadrat : {square(result)}')
print(f'Penjumlahan : {addition(result)}')
print(f'Pengurangan : {reduction(result)}')
print(f'Perkalian : {multiply(result)}')
print(f'Pembagian : {division(result)}')
