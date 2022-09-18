from selenium import webdriver
from selenium.webdriver.common.by import By
import time # 페이지 로딩을 기다리는데 사용할 모듈

# send_keys("") : 글자 입력
# clear() : 글자 지움
# click() : 클릭

chrome_path = 'C:\py_khs\chromedriver.exe'  # 크롬드라이버의 경로
url = 'https://naver.com/' # 들어가고 싶은 url
id = ''
pw = ''

browser = webdriver.Chrome(chrome_path) # 크롬드라이버 실행
browser.get(url) # 크롬 드라이버에 url 주소 넣고 실행
time.sleep(0.3) # 페이지가 완전히 로딩되도록 3초 동안 기다림
browser.find_element(By.XPATH,'//*[@id="account"]/a').click()
time.sleep(0.3)

# 아이디와 비밀번호를 이용한 방법
# browser.find_element(By.XPATH,'//*[@id="login-email-field"]').send_keys(id)
# browser.find_element(By.XPATH,'//*[@id="login-password-field"]').send_keys(pw)
# browser.find_element(By.XPATH,'//*[@id="log-in-button"]').click()

# github으로 로그인
browser.find_element(By.XPATH,'//*[@id="login-with-github"]').click()
browser.find_element(By.XPATH,'//*[@id="login_field"]').send_keys(id)
browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(pw)

browser.switch_to.window(browser.window_handles[-1]) # 최신 팝업창으로 이동
browser.switch_to.window(browser.window_handles[0]) # 원래 창으로 이동

browser.close() # 크롬 창 닫기