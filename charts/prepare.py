import os
import pandas
import zipfile


def unZip():
    """unzip zip file(Data.zip) to ./Data"""
    zip_file = zipfile.ZipFile("Data.zip")
    if not os.path.isdir("Data"):
        os.mkdir("Data")
    for file in zip_file.namelist():
        zip_file.extract(file, "Data")
    zip_file.close()


def getData():
    """Aquire information from a csv file"""
    data = [[] for _ in range(365)]
    lst = os.listdir("Data")
    for i in range(365):
        f = pandas.read_csv("Data/" + lst[i], encoding="utf-8")
        data[i] = f[["城市", "新增确诊"]].values.tolist()
    result = data[0]
    for i in range(365):
        for j in range(364):
            result[j][1] += data[i][j][1]

    i = 0
    while i < len(result):
        if result[i][1] == 0:
            result.remove(result[i])
            i -= 1
        i += 1

    return result
