# Closure

# def generator(y):
#     def multi(x):
#         return x * y
#     return multi


# try1 = generator(int(input("Masukkan nilai 1 - 1 : ")))
# print(try1(int(input("Masukkan nilai 1 - 2: "))))

# try2 = generator(int(input("Masukkan nilai 2 - 1: ")))
# print(try2(int(input("Masukkan nilai 2 - 2: "))))


# Decorator
def generator(func):
    def inner(x, y):
        return func(x, y)
    return inner


@generator
def multi(x, y):
    print(x * y)


def inputVal():
    return int(input())


print("Proses 1 : ")
multi(inputVal(), inputVal())

print("Proses 2 : ")
multi(inputVal(), inputVal())
