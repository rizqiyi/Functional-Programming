listOfDict = [
    {"nama": "Ahmad", "jurusan": "Informatika", "semester": 2, "angkatan": ""},
    {"nama": "", "jurusan": "Pertanian", "semester": "", "angkatan": 2017},
    {"nama": "Insan", "jurusan": "", "semester": 3, "angkatan": ""},
    {"nama": "Malik", "jurusan": "", "semester": 6, "angkatan": 2018},
    {"nama": "", "jurusan": "Kehutanan", "semester": "", "angkatan": 2015},
]

data = ["nama", "jurusan", "semester", "angkatan"]


def inputValues(rows, keys):
    for i in range(0, len(rows)):
        b = []
        for j in range(0, len(keys)):
            if(rows[i].get(keys[j]) == ""):
                if(keys[j] == "semester" or keys[j] == "angkatan"):
                    b = int(
                        input(f'Key [{j + 1}] Value [{i + 1}] ({str(keys[j]).capitalize()}) : '))
                    rows[i].update({keys[j]: b})
                else:
                    c = input(
                        f'Key [{j + 1}] Value [{i + 1}] ({keys[j].capitalize()}) : ')
                    rows[i].update({keys[j]: c})
    return rows


inputValues(listOfDict, data)

print(f'\nResult : \n{listOfDict}')
