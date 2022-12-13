print('-----------第一題-----------')
year=1911+(eval(input("input year(民國):")))
# print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print('閏年')
else:
    print('平年')


print('-----------第二題-----------')
a,b,c=eval(input('input x**2的係數，x**1的係數，常數係數:'))
D=(b**2)-(4*a*c)
e=((-b)+(D**0.5))/(2*a)
f=((-b)-(D**0.5))/(2*a)
x=(-b)/(2*a)
if(D>0):
    print(f'相異解 x1={e},x2={f}')
elif(D==0):
    print(f'相似解 x1={x},x2={x}')
else:
    print('無解')


print('-----------第三題-----------')
c,e,m=eval(input('input 國 英 數'))
num=(c+e+m)/3
# print(num)
if((num>=90)&(num<=100)):
    print('A')
elif((num>=80)&(num<90)):
    print('B')
elif((num>=70)&(num<80)):
    print('C')
elif((num>=60)&(num<70)):
    print('D')
else:
    print('不及格')
    