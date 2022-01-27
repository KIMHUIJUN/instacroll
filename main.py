from urllib.parse import quote_plus as qp
from urllib.request import urlopen
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import urllib.request
from selenium.webdriver.common.keys import Keys

baseurl = "https://www.instagram.com/explore/tags/"
plusurl = input('검색할 태그를 입력하세요: ')
url = baseurl + qp(plusurl)

target_url = "https://www.instagram.com"
options = webdriver.ChromeOptions()

driver = webdriver.Chrome("C:/Users/chromedriver.exe")
driver.get(target_url)

time.sleep(2)

login_id = ''  # 아이디
login_pw = ''  # 비밀번호

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login_id)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(login_pw)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.sqdOP.yWX7d.y3zKF').click()
time.sleep(3)  # 로그인 저장 나중에

driver.find_element(By.CSS_SELECTOR, '.aOOlW.HoLwm').click()
time.sleep(3)  # 설정 나중에

driver.get(url)
time.sleep(5)

n = 1
n2 = 1
s = 1
for i in range(3):  # 인기 사진은 무조건 9개임
    a = 1
    for p in range(3):
        thumbnails = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/article/div[1]/div/div/div[{}]/div[{}]/a/div/div[1]/img'.format(n, a)).get_attribute('src')
        time.sleep(5)
        urllib.request.urlretrieve(thumbnails, "{}.jpg".format(s))
        a += 1
        s += 1
    n += 1

body = driver.find_element(By.CSS_SELECTOR, 'body')
for x in range(2):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

for i in range(20):  # 최근사진 갯수 = () x 3
    a = 1

    for p in range(3):
        thumbnails = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/article/div[2]/div/div[{}]/div[{}]/a/div[1]/div[1]/img'.format(n2, a)).get_attribute('src')
        time.sleep(3)
        urllib.request.urlretrieve(thumbnails, "{}.jpg".format(s))
        time.sleep(3)
        a += 1
        s += 1
    time.sleep(3)

    for x in range(1):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)


    n2 += 1


