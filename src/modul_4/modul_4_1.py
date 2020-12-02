number = [input("Masukkan Nomor : ")
          for _ in range(int(input("Masukkan jumlah nomor : ")))]


def wrapper(firstParams):
    def phone(number):
        firstParams(["+62"+c[-10:-5]+""+c[-5:] for c in number])
    return phone


@wrapper
def sort(number):
    print(*sorted(number), sep='\n')


print('\nHasil pengurutan nomor : ')
sort(number)
