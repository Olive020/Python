import requests as re
# url='網站'
# r=re.get(url)
# #存圖
# with open('123.jpg',mode='wb') as file:
#     file.write(r.content)
# #存pdf
# with open('123.pdf',mode='wb') as file:
#     file.write(r.content)

url='https://httpbin.org/get'
r=re.get(url)
print(r.text)