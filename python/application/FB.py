# from this import d
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

PATH="C:/Users/Administrator/Desktop/chromedriver win32/chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://zh-tw.facebook.com/")

email=driver.find_element_by_name("email")
password=driver.find_element_by_name("pass")

WebDriverWait(driver,30).until(
    EC.presence_of_all_elements_located((By.ID,"pass"))
)


email.clear
password.clear()
email.send_keys("0973880806")
password.send_keys("w0973880806")
password.send_keys(Keys.RETURN)
