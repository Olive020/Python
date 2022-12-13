# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print("最後的n=",n)

#0,2跳過,因為continue
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("最後的n:",n)

# sum=0
# for n in range(11):#=range(1,11)
#     sum+=n
# else:
#     print(sum)  #0+1+,,,10


n=int(input("輸入一個正整數:"))
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break
else:
    print("沒有整數平方根")