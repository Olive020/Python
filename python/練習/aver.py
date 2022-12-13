a=int(input("成績數量:"))
i=0
sum=0
# while i<a:
#     print("成績",i+1)
#     x=int(input("成績:"))
#     sum+=x
#     i+=1
# aver=sum/a
# print("平均值:",aver)

for i in range(a):
    print("成績",i+1)
    x=int(input("成績:"))
    sum+=x
aver=sum/a
print("平均值=",aver)
