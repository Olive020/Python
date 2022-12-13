import requests 
# import urllib.request as rep 
import bs4


url='https://www.104.com.tw/jobs/search/?keyword=python&order=1&jobsource=2018indexpoc&ro=0'
# request=req.Request(url,headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
# })
htmlFile=requests.get(url)
objSoup=bs4.BeautifulSoup(htmlFile.text,'lxml')
job=objSoup.find_all('article',class_='js-job-item')

for i in job:
    print("company name:", i.get('data-cust-name'))
    print("job title name:", i.get('data-job-name'))