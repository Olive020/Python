from ctypes import sizeof
from email import header
from pydoc import classname
from matplotlib.pyplot import title
import requests as re
from openpyxl import Workbook
import bs4
import urllib.request as req
from sympy import classify_ode
import xlwt
import xlrd
My_header ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

a=list()
b1=list()
b2=list()
c=list()
e=0
run=0
x=0

fn='test.xls'
file=open("test.xls",mode="w",encoding="utf-8")
data=['company','pay','place']
wb=xlwt.Workbook()
sh=wb.add_sheet('sheet1',cell_overwrite_ok=True)
for w in range(len(data)):
    sh.write(0,w,data[w])
url1='https://www.1111.com.tw/search/job?d0=140212%2C140206%2C140201&page='
url2='&act=load_page&v=1650347748398'



for i in range(2,40):
    url=url1+str(i)+url2
    request=req.Request(url,headers=My_header)
    with req.urlopen(request) as reaponse:
        data=reaponse.read().decode("utf-8")
    
    root=bs4.BeautifulSoup(data,"html.parser")
    titles_company=root.find_all("h6")
    titles=root.find_all("div")
    # print(titles)
    for company in titles_company:
        # print(company.string) 
        a.append(company.string)
        e+=1
    for salary in titles:
        if((salary.string)==None or len(salary.string)<5):
            continue
        else:
            # print(salary.string)
            b1.append(salary.string)
    # print('_______________________')
    # print(len(b1))
    for j in range(0,len(b1),2):
        b2.append(b1[j])
        # print(b1[j])
    
    for x in range(e-1):
        sh.write(x+1,0,a[x])
        sh.write(x+1,1,b2[x])
        # sh.write(x+1,1,b1[x+run])
        

url='https://www.1111.com.tw/search/job?d0=140212,140206,140201'
htmlFile=re.get(url,headers=My_header)

objSoup=bs4.BeautifulSoup(htmlFile.text,'lxml')
#公司
jobc=objSoup.find_all('h6',class_='job_item_company mb-1 digit_5 body_3')
#薪水
jobr=objSoup.find_all('div',class_='job_item_detail_salary ml-3 font-weight-style digit_6')
#地點
jobp=objSoup.find_all('a',class_='job_item_detail_location mr-3 position-relative')

for i in jobc:
    # print("company name:", i.string)
    a.append( i.string)
    e+=1
for i in jobr:
    # print("pay:", i.string)
    b2.append( i.string)
# for i in jobp:
#     print("pay:", i.string)
#     c.append( i.string)

for x in range(e-1):
    sh.write(x+1,0,a[x])
    sh.write(x+1,1,b2[x])
    # sh.write(x+1,1,b1[x+run])
   


wb.save(fn)
file.close()
print("存檔完畢")