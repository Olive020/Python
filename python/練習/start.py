#我的第一支python程式
# print("Hello world")
# #布林值
# True
# False
# import antigravity
# import random as ra
# import math as ma
# print(3.14%1)
# x,y,z=1,2,3
# z=2//1
# print(ma.pi)
# print(x,y,z)
# a=-0.2**-0.6
# print('a==',a)
# s=int(input("1  2  :"))
# n=int(input("?"))
# b=ra.choice(["4","5","6","7"])
# for i in range(3):
#     if s==1:
#         a=ra.choice(["cbefke","vecebuk","erhrh"])
#         c=ra.choice(["cbefke","vecebuk","erhrh"])
#         input("why?")
#         print(a)
#         input("怎麼了?")
#         print(c)

def fun(x):
    y2=((x**3)+x+1)%p
    return y2

p=23
xt=[]
yt=[]
for x in range(0,p):
    for y in range(0,p):
        if (y**2)%p==fun(x):
            xt.append(x)
            yt.append(y)

import matplotlib.pyplot as pl
pl.plot(xt,yt,'r.')
pl.ylabel('mod'+str(p)+' ecc')
pl.show