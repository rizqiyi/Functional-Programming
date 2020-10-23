# Kegiatan 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in range(0, len(numbers)):
    if(numbers[i] > 0):
        for j in range(2, numbers[i]):
            if(numbers[i] % j) == 0:
                if(numbers[i] % 2) == 1:
                    print(numbers[i], "ganjil")
                    break
                print(numbers[i], "genap")
                break
        else:
            if(numbers[i] == 1):
                print(numbers[i], "ganjil")
            else:
                print(numbers[i], "prima")


# Kegiatan 2

def odd_numbers(x): return x % 2 == 1


isEvenNumber = lambda number: number % 2 = 0

def prime_numbers(x):
    if(x < 2):
        return False
    for i in range(2, x):
        if(x % i) == 0:
            return False
    return True


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in lists:
    if(prime_numbers(i)):
        print(i, "prima")
    elif(odd_numbers(i)):
        print(i, "ganjil")
    else:
        print(i, "genap")
