# #儲存檔案
file=open("date.txt",mode="w")#開啟
file.write("Hello file\nSecond Line")#操作
file.close()#關閉
# #讀取檔案

# file=open("date.txt",mode="w",encoding="utf-8")#開啟
# file.write("中文測試\n")#操作
# file.close()#關閉

with open("date.txt",mode="w",encoding="utf-8") as file:
    file.write("中文測試\n")


# #讀取
# with open("date.txt",mode="r",encoding="utf-8") as file:
#     date=file.read()
# print(date)


# with open("date.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")
# #把數字一行一行的讀取出來,並算總和
# sum=0
# with open("date.txt",mode="r",encoding="utf-8") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

#用json格式讀取檔案
# import json
# with open("config.json",mode="r") as file:
#     date=json.load(file)
# print(date)#date:字典資料
# print("name:",date["name"])
# print("version:",date["version"])

#修改json資料
# import json
# with open("config.json",mode="r") as file:
#     date=json.load(file)
# print(date)
# date["name"]="New Name"#修改變數資料
# #把最新的資料副寫進檔案
# with open("config.json",mode="w") as file:
#     json.dump(date,file)

