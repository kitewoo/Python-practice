from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome   
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import time
import os
from mkdir import makedir #직접 만든 모듈(같은 작업 폴더 안에 있다.)
import tqdm
from urllib import request


# instagram login 

driver = Chrome("C:/Users/tt/Desktop/pycode/chromedriver") # 프로그램 연결
driver.get("https://www.instagram.com/")
  
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

a = makedir(keyword)

try :
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')))
    
except :
    print("오류가 발생했습니다.")

driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click() #검색되면 첫 태그 클릭

try :
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]'))) 
    
except :
    print("오류가 발생했습니다.")

driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click() #첫 게시물 클릭

try :
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/div[2]'))) 
    
except :
    print("오류가 발생했습니다.")

img_tag = []
for i in range(10):
    try:
        html = driver.page_source
        soup = bs(html, "html.parser")
        try: 
            img = soup.find("div", class_="_97aPb C2dOX")
            img_src = img.select_one('.KL4Bh').img['src']
            img_tag.append(img_src)

        except:
            img = soup.find("div", class_='_97aPb C2dOX HCDIA')
            img_src = img.select_one('.KL4Bh').img['src']
            img_tag.append(img_src)

        if i == 0:
            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/button").click()
            try :
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[2]'))) 
    
            except :
                print("오류가 발생했습니다.")
        else:
            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/button").click()
            try :
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[2]'))) 
    
            except :
                print("오류가 발생했습니다.")
    except:
                
        if i == 0:
            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/button").click()
            try :
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[2]'))) 

            except :
                print("오류가 발생했습니다.")
        else:
            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/button").click()
            try :
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[2]'))) 

            except :
                print("오류가 발생했습니다.")
        pass

fdir="C:/Users/tt/Desktop/pycode/images/"+keyword+'/'

num = 1
for tag in img_tag:
    img_name = fdir + keyword + str(num) + ".jpg"
    request.urlretrieve(tag, img_name)
    time.sleep(1)
    num += 1

while True:
    pass
