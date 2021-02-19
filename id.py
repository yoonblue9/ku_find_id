from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import urllib.request

headers = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
# 크롬드라이버 경로
path = "PATH to chromedriver"
options = webdriver.ChromeOptions()

options.add_argument("headless")
options.add_argument("no-sandbox")

options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument(headers)

driver = webdriver.Chrome(path, chrome_options=options)
driver.get("https://sugang.korea.ac.kr")
driver.switch_to.frame("Main")
title = driver.title
for i in range(1, 200):
    # 2021320을 자기 학과 코드로 바꾸기 (현재는 컴과)
    id = "2021320" + "%03d" % i
    # pw에 주민번호 뒷자리 입력
    pw = ""
    try:
        driver.find_element_by_xpath('//*[@id="id"]').clear()
        driver.find_element_by_xpath('//*[@id="id"]').send_keys(id)
        driver.find_element_by_xpath('//*[@id="pwd"]').clear()
        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(pw)
        driver.find_element_by_xpath('//*[@id="btn-login"]').send_keys(Keys.ENTER)
    except:
        print(int(id) - 1)
        break
driver.close()
