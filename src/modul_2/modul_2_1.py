b = [1, 4, 9]


def biasa(x):
    b = []
    for i in range(0, len(x)):
        b.append(x[i] * x[i])
    return b


print(biasa(b))


x = map(lambda x: x*x, b)
print(list(x))


a = [1, 2, 3, 4]


def listb(x):
    b = []
    for i in range(0, len(x)):
        if(x[i] % 2 == 1):
            b.append(x[i])
    return b


print(listb(a))


g = filter(lambda x: x % 2 == 1, a)
print(list(g))
