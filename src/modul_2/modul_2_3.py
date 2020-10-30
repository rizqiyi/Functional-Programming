# Kegiatan 3
result = []


def inputValues(rows, columns):
    for i in range(rows):
        a = []
        for j in range(columns):
            a.append(int(input(f'[{i}][{j}] : ')))
        result.append(tuple(a))
    return tuple(result)


def square(val):
    row = []
    for x in range(0, len(val)):
        column = []
        for z in range(0, len(val[x])):
            square = val[x][z] * val[x][z]
            column.append(square)
        row.append(tuple(column))
    return tuple(row)


def addition(val):
    row = []
    for x in range(0, len(val)):
        column = []
        for z in range(0, len(val[x])):
            resultAdd = val[x][z] + val[x][z]
            column.append(resultAdd)
        row.append(tuple(column))
    return tuple(row)


def reduction(val):
    row = []
    for x in range(0, len(val)):
        column = []
        for z in range(0, len(val[x])):
            resultReduction = val[x - 1][z - 1] - val[x][z]
            column.append(resultReduction)
        row.append(tuple(column))
    return tuple(row)


def multiply(val):
    row = []
    for x in range(0, len(val)):
        column = []
        for z in range(0, len(val[x])):
            resultMult = val[x - 1][z - 1] * val[x][z]
            column.append(resultMult)
        row.append(tuple(column))
    return tuple(row)


def division(val):
    row = []
    for x in range(0, len(val)):
        column = []
        for z in range(0, len(val[x])):
            resultDiv = val[x - 1][z - 1] / val[x][z]
            column.append(round(resultDiv, 2))
        row.append(tuple(column))
    return tuple(row)


rows = int(input("Masukkan jumlah baris : "))
columns = int(input("Masukkan jumlah kolom : "))
print("Masukkan nilai : ")
print(f'\nInput : {inputValues(rows, columns)}\n')

print(f'Kuadrat : {square(result)}')
print(f'Penjumlahan : {addition(result)}')
print(f'Pengurangan : {reduction(result)}')
print(f'Perkalian : {multiply(result)}')
print(f'Pembagian : {division(result)}')
