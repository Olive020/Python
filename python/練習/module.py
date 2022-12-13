# import sys
# print(sys.platform) #作業系統
# print(sys.maxsize) #整數型態max

#建立geometry模組並載入
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)

import sys
sys.path.append("modules")
print(sys.path)
print("-------------------")
from modules import geometry
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
print(geometry.distance(x1,y1,x2,y2))