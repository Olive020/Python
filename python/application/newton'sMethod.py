import math as ma

from requests.models import default_hooks
co=[0]*100
power=[0]*100
deco=[0]*100
depower=[0]*100
coo=[0]*100
c=0
d=0
w=0
for i in range(100):

    z=input("")
    if z=='*':
        a=float(input(""))
        b=float(input("*"))
        co[i]=a*b
    if z=='/':
        a=float(input(""))
        b=float(input("/"))
        co[i]=a/b
    if z=='=':
        a=i
        break
    else:
        co[i]=int(z)


    q=input("x^")
    if q=='*':
        a=float(input(""))
        b=float(input("*"))
        power[i]=a*b
    if q=='/':
        a=float(input(""))
        b=float(input("/"))
        power[i]=a/b
    else:
        power[i]=float(q)
    
    deco[i]=float(power[i])*float(co[i])
    depower[i]=float(power[i])-1
    # print(co[i],power[i],deco[i],depower[i])
x=float(input("x1:"))
for i in range(10):
    # print('a=',a)
    # print('co=',co)
    # print('power=',power)
    for w in range(a):
        print('w=',w)
        print('x=',x)
        x=-0.2
        c+=co[w]*ma.pow(x,power[w])
        d+=deco[w]*ma.pow(x,depower[w])
        # print(c,d)
    x=x-(c/d)
    print(x)
    c=0
    d=0