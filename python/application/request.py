import urllib.request as request
src="http://www.ntu.edu.tw/"
with request.urlopen(src) as request:
     data=request.read().decode("utf-8") #該網站原始碼
print(data)

