from os import read


with open("data.txt",mode="w",encoding="utf-8")as file:
    file.write("測試\n")
with open("data.txt",mode="r",encoding="utf-8")as fil:
    data=fil.read()
print(data)