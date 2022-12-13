import requests as re
import xlwt
import xlrd
import os
# import urllib.request as rep 
import bs4
a=list()
b=list()
c=list()
e=0
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
url='https://www.1111.com.tw/search/job?c0=101800&d0=140202'


htmlFile=re.get(url,headers=header)

objSoup=bs4.BeautifulSoup(htmlFile.text,'lxml')
#公司
jobc=objSoup.find_all('h6',class_='job_item_company mb-1 digit_5 body_3')
#薪水
jobr=objSoup.find_all('div',class_='job_item_detail_salary ml-3 font-weight-style digit_6')
#地點
jobp=objSoup.find_all('a',class_='job_item_detail_location mr-3 position-relative')
fn='1111.xls'
file=open("1111.xls",mode="w",encoding="utf-8")
data=['company','pay','place']
wb=xlwt.Workbook()
sh=wb.add_sheet('sheet1',cell_overwrite_ok=True)

for w in range(len(data)):
    sh.write(0,w,data[w])

for i in jobc:
    print("company name:", i.string)
    a.append( i.string)
    e+=1
for i in jobr:
    print("pay:", i.string)
    b.append( i.string)
for i in jobp:
    print("pay:", i.string)
    c.append( i.string)

for x in range(e-1):
    sh.write(x+1,0,a[x])
    sh.write(x+1,1,b[x])
    sh.write(x+1,2,c[x])
# print(file)
wb.save(fn)
file.close()
print("存檔完畢")