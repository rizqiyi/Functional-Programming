# Kegiatan 2

List1 = ["jurusan", "praktikum", "kampus", "tahun"]
List2 = ["informatika", "fungsional", "UMM", "2020"]


def lists(a1, a2):
    a = []
    for i in range(0, len(a1)):
        for j in range(0, len(a2)):
            if(i == j):
                a.append(a1[i] + a2[j])
    return a


def listsCapital(a1, a2):
    a = []
    for i in range(0, len(a1)):
        for j in range(0, len(a2)):
            if(i == j):
                a.append(str(a1[i]).capitalize() + str(a2[j]).capitalize())
    return tuple(a)


def dictionary(a1, a2):
    h = {}
    for i in range(0, len(a1)):
        for j in range(0, len(a2)):
            if(i == j):
                a = {a1[i]: a2[j]}
                h.update(a)
    return h


print(lists(List1, List2))
print(str(lists(List1, List2)).lower())
print(listsCapital(List1, List2))
print(str(listsCapital(List1, List2)).upper())
print(dictionary(List1, List2))
