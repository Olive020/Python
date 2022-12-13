import random
print(random.uniform(0,1000))
x=input("請輸入成績:")
x=int(x)#==   x=int(input("請輸入成績:"))
if x>70:
    print("及格")
elif x>=60:
    print("擦邊")
else:
    print("重補修")
