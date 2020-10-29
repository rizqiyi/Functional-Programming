# Map
b = [1, 4, 9]

# method biasa


def biasa(x):
    b = []
    for i in range(0, len(x)):
        b.append(x[i] * x[i])
    return b


# Print biasa
print(biasa(b))

# print pake map
x = map(lambda x: x*x, b)
print(list(x))


# Filter
a = [1, 2, 3, 4]


def listb(x):
    b = []
    for i in range(0, len(x)):
        if(x[i] % 2 == 0):
            b.append(x[i])
    return b


# filter biasa
print(listb(a))

# print pake filter
g = filter(lambda x: x % 2 == 0, a)
print(list(g))
