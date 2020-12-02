from operator import itemgetter

data = [
    {"nama_depan": "Afwun", "nama_belakang": "Shiddiq",
        "usia": 20, "jenis_kelamin": "laki-laki"},
    {"nama_depan": "Rosalia", "nama_belakang": "Benarti",
        "usia": 21, "jenis_kelamin": "perempuan"},
    {"nama_depan": "Ahmad", "nama_belakang": "Sentosa",
        "usia": 20, "jenis_kelamin": "laki-laki"},
    {"nama_depan": "Mary", "nama_belakang": "Jane",
        "usia": 19, "jenis_kelamin": "perempuan"},
    {"nama_depan": "Muhammad", "nama_belakang": "Jito",
        "usia": 27, "jenis_kelamin": "laki-laki"},
    {"nama_depan": "Bunga", "nama_belakang": "Lestari",
        "usia": 26, "jenis_kelamin": "perempuan"},
]


def wrapper(firstParams):
    def phone(*number):
        firstParams(*number)
    return phone


@wrapper
def sort(number):
    temp = []

    t = sorted(number, key=itemgetter('usia'))

    for i in t:
        fullName = i.get("nama_depan") + " " + i.get("nama_belakang")

        temp.append("Mr. " + fullName if i.get("jenis_kelamin")
                    == "laki-laki" else "Ms. " + fullName)

    print(*temp[0:3], sep="\n")


sort(data)
