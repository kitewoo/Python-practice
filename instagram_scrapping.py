from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome   
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import time
import os
import tqdm
from urllib import request

driver = Chrome("C:/Users/tt/Desktop/pycode/chromedriver")
driver.get('https://www.instagram.com/')

 
try :
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button'))) #괄호 3개임. ㄷㄷ
    print(elem)

except :
    print("오류가 발생했습니다.")

userid = input("아이디를 입력하세요: ")
userpw = input("비밀번호를 입력하세요: ")

input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input') #아이디 칸 접근 변수 설정
input_id.clear()
input_id.send_keys(userid)

input_pw = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input') #비밀번호 칸 접근 변수 설정
input_pw.clear()
input_pw.send_keys(userpw)

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button').click()

try :
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div'))) #괄호 3개임. ㄷㄷ
    
except :
    print("오류가 발생했습니다.")

keyword = input("검색어를 입력하세요: ")

input_keyword = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input') #검색어 접근 변수 설정
input_keyword.clear()
input_keyword.send_keys(keyword) #send_keys : 텍스트 입력 후 enter 


try :
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')))
    
except :
    print("오류가 발생했습니다.")

driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click() #검색되면 첫 태그 클릭


try :
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]'))) 
    
except :
    print("오류가 발생했습니다.")

folder = os.mkdir(keyword)

'''import math
from tqdm import tqdm 
import re

html = driver.page_source
soup = bs(html,'html.parser')
concnt = soup.find('span', class_='g47SY').get_text()
concnt = re.sub(",","",concnt)

count_down = math.floor(int(concnt)/8)



tag1 = []

for i in tqdm(range(count_down)):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    html = driver.page_source
    soup = bs(html,'html.parser')
    contents = soup.find_all('div', class_='Nnq7C weEfm')
    for content in contents:
        con = content.find_all('div',class_="v1Nh3 kIKUG _bz0w")
        for c in con:
            tag = c.find('img')['src']
            if tag not in tag1:
                tag1.append(tag)
    time.sleep(1.5)'''


import math
from tqdm import tqdm 
import re

html = driver.page_source
soup = bs(html,'html.parser')
concnt = soup.find('span', class_='g47SY').get_text()
concnt = re.sub(",","",concnt)

count_down = math.floor(int(concnt)/8)



tag1 = []

while len(tag1) != int(concnt):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    html = driver.page_source
    soup = bs(html,'html.parser')
    contents = soup.find_all('div', class_='Nnq7C weEfm')
    for content in contents:
        con = content.find_all('div',class_="v1Nh3 kIKUG _bz0w")
        for c in con:
            tag = c.find('img')['src']
            if tag not in tag1:
                tag1.append(tag)
    time.sleep(1.5)
    
    if len(tag1) == int(concnt):
        print(len(tag1))
        
fdir = "C:/Users/tt/Desktop/pycode/"+keyword+'/'
for a in range(len(tag1)):
    img_name = fdir + keyword + str(a) + ".jpg"
    request.urlretrieve(tag1[a],img_name)

  

    
