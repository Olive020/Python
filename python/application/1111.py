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
url='https://www.1111.com.tw/search/job?c0=101800&d0=140202'
htmlFile=re.get(url)

objSoup=bs4.BeautifulSoup(htmlFile.text,'lxml')
jobc=objSoup.find_all('div',class_='item__job-organ-m')
jobr=objSoup.find_all('i',class_='item__job-prop-item item__job-prop-salary')
jobp=objSoup.find_all('i',class_='item__job-prop-item item__job-prop-workcity')
fn='1111.xls'
file=open("1111.xls",mode="w",encoding="utf-8")
data=['company','pay','place']
wb=xlwt.Workbook()
sh=wb.add_sheet('sheet1',cell_overwrite_ok=True)
for w in range(len(data)):
    sh.write(0,w,data[w])
for i in jobc:
    print("company name:", i.get('aria-label'))
    a.append( i.get('aria-label'))
    e+=1
for i in jobr:
    print("pay:", i.get('aria-label'))
    b.append( i.get('aria-label'))
for i in jobp:
    print("pay:", i.get('aria-label'))
    c.append( i.get('aria-label'))

for x in range(e-1):
    sh.write(x+1,0,a[x])
    sh.write(x+1,1,b[x])
    sh.write(x+1,2,c[x])
# print(file)
wb.save(fn)
file.close()
print("存檔完畢")