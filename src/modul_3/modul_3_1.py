listOfDict = [
    {"barang": "komputer", "jumlah": 50, "kualitas": "baru", "harga": 20000000},
    {"barang": "laptop", "jumlah": 2, "kualitas": "baru", "harga": 10000000},
    {"barang": "keyboard", "jumlah": 20, "kualitas": "baru", "harga": 500000},
    {"barang": "mouse", "jumlah": 30, "kualitas": "baru", "harga": 250000},
    {"barang": "monitor", "jumlah": 10, "kualitas": "baru", "harga": 1500000},
]

# Jika nomor 1 dijalankan maka akan ada error di beberapa line, kalo ga pake command aja
# karena tidak menambahkan key (sudah di-pop duluan di nomor 1)
# Nomor 1

# def printSpesificKeys(val):
#     for i in range(0, len(val)):
#         val[i].pop("barang") and val[i].pop("kualitas")
#     return val


# print(f'Nomor 1\n{printSpesificKeys(listOfDict)}')

# Nomor 2


def clearItems(val, idx):
    return val.pop(idx)


clearItems(listOfDict, 1)

print(f'Nomor 2 \n{listOfDict}\n')


# Nomor 3
print("Nomor 3")


def getDictKeys(val):
    for i in range(0, len(val)):
        return list(val[i].keys())


def printAllKeysAndValues(val, keys):
    for i in range(0, len(val)):
        for j in range(0, len(val[i])):
            print(
                f'{str(keys[j]).capitalize()} :  {"Rp. " + "{:,}".format(val[i].get(keys[j])) if keys[j] == "harga" else val[i].get(keys[j])}')
        print("-----")


# printAllKeysAndValues(listOfDict, getDictKeys(listOfDict))


# Nomor 4
newValues = ["meja", 10, "bekas", 1000000]


def insertNewValues(val, keys, root):
    a = {}
    for i in range(0, len(keys)):
        for j in range(0, i + 1):
            a.update({keys[i]: val[j]})
    root.append(a)
    return root


print(
    f'\nNomor 4\n{insertNewValues(newValues, getDictKeys(listOfDict), listOfDict)}\n')

# printAllKeysAndValues(listOfDict, getDictKeys(listOfDict))
# print("\n")
# Nomor 5
listUpdateValues = [1000, 1000, 1000, 1000, 1000]


def updateLastValues(updateVal, root):
    for i in range(0, len(root)):
        root[i].update({"harga": updateVal[i]})
    return root


print(
    f'Nomor 5\n{updateLastValues(listUpdateValues, listOfDict)}\n')

# Nomor 6
print("Nomor 6")
printAllKeysAndValues(listOfDict, getDictKeys(listOfDict))

# Nomor 7
spesificValues = ["jumlah", "harga", "kualitas"]
spesificKey = [0, 1, 3]
newValues2 = [100, 2000000, "original"]


def updateSpesificValues(newValues, root, keys, rows):
    for i in range(0, len(keys)):
        root[keys[i]].update({rows[i]: newValues[i]})
    return root


print(
    f'Nomor 7\n{updateSpesificValues(newValues2, listOfDict, spesificKey, spesificValues)}')

# Nomor 8
print("\nNomor 8")
printAllKeysAndValues(listOfDict, getDictKeys(listOfDict))

# Nomor 9


def sumStock(val):
    stock = 0
    for i in range(0, len(val)):
        stock += val[i].get("jumlah")
    return stock


def totalIncome(val):
    income = 0
    for i in range(0, len(val)):
        income += val[i].get("harga")
    return income


print("\nNomor 9")
print(f'Total Stok : {sumStock(listOfDict)}')
print(
    f'Total Untung : {"Rp. " + "{:,}".format(totalIncome(listOfDict))}\n')


# Nomor 10
def combineDictionary(root):
    temp = []
    for i in range(0, len(root)):
        temp.append(root[i].get("barang") + root[i].get("kualitas"))
    return temp


print(f'Nomor 10\n{combineDictionary(listOfDict)}')
