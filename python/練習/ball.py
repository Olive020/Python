ball=50
i=0
while(i==0):
    x=int(input("P1要拿多少顆球?"))
    if(x>3):
        x=int(input("重新輸入"))
    ball-=x
    if ball==0:
        print("x is lose")
        break
    print(ball)
    y=int(input("P2要拿多少顆球?"))
    if(y>3):
        y=int(input("重新輸入"))
    ball-=y
    if ball==0:
        print("y is lose")
        break
    print(ball)