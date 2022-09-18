from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip    # 클립보드를 사용하여 복사-붙여넣기를 간편하게 할 수 있는 모듈

chrome_path = 'C:\py_khs\chromedriver.exe'  # 크롬드라이버의 경로
url = 'https://www.naver.com/'

browser = webdriver.Chrome(chrome_path)
browser.get(url)
browser.find_element(By.XPATH,'//*[@id="account"]/a').click()
pyperclip.copy("")    # id 
browser.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')