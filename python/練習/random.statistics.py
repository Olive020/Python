#隨機模組
import random
#隨機選取
# data=random.choice([1,5,6,4,78,92])#隨機選一
# print(data)
data=random.sample(["1","5","6","4","78","92"],3)
for i in range(3):
    print(data[i])

#隨機調換順序
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)

#隨機取得亂數
# data=random.random()#0.0到1.0間的隨機亂數
# data=random.uniform(0.0,1.0)
# print(data)

#常態分配亂數
data=random.normalvariate(100,10)#平均數100,標準差10
print(data)

#統計模組
# import statistics as stat
# # data=stat.mean([1,4,5,8])#aver
# # data=stat.median([1,2,3,4,5,8,50])#中位數
# data=stat.stdev([1,3,4,5,8])#標準差
# print(data)
