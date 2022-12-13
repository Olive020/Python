x=int(input("請輸入數字1:"))
y=int(input("請輸入數字2:"))
z=input("輸入計算方法+,-,*,/,%:\n")
if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    print(x/y)
elif z=="%":
    print(x%y)
else:
    print("錯誤")