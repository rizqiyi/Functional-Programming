# Map
def lists(x):
    return x * x


b = [1, 4, 9]

z = []

for i in b:
    z.append(lists(i))

# Print biasa
print(z)

x = map(lists, b)
# print pake map
print(list(x))

# Filter

a = [1, 2, 3, 4]


def listb(x):
    b = []
    for i in range(0, len(x)):
        if(x[i] % 2 == 0):
            b.append(x[i])
    return b


print(listb(a))


g = filter(lambda x: x % 2 == 0, a)

print(list(g))
