n=0
sum=0
while(n!=-1):
    n=int(input("1加到:"))
    if n==-1:
        break
    for i in range(0,n+1):
        sum+=i
    print("1加到%d=%d"%(n,sum)) 
    sum=0   
print("end")