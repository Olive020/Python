# def multiply(n1,n2):
#     print(n1*n2)
#     return 10
 
# value=multiply(3,4)
# print(value)

def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)
x=int(input("x="))
calculate(x)