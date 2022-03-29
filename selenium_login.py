#셀레니움으로 로그인하기
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
import pyperclip #복사/붙여넣기 클립보드 기능 모듈 ㅣ copy() : 클립보드에 텍스트 복사 paste() : 클립보드에 저장된 텍스트 붙여넣기
import time
from urllib import request    # 이미지 다운로드에 사용
from bs4 import BeautifulSoup as bs #크롤링 
from tqdm import tqdm #진행률 표시 
from urllib.parse import quote_plus

userid = input('아이디 :' )
userpw = input('패스워드: ') 

def login(userid, userpw): 
    driver = Chrome('C:/Users/tt/Desktop/pycode/chromedriver.exe') 
    driver.get("https://www.instagram.com/accounts/login/") #크롬제어창으로 주소 열기

    # By는 html 문서를 어떤 엘리먼트 형태로 가져올 것인지 지정하는 것. 여기서는 XPATH로 해봤다. 

    # 셀레니움 대기 기능 : NosuchelementException 에러는 선택되는 html이 존재하기 전에 접근을 시도했기 때문에 발생한다.  
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.TAG_NAME, 'p')))

    input_id=driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input' )
    input_id.clear()
    input_id.send_keys(userid)

    input_pw=driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')
    input_pw.clear()
    input_pw.send_keys(userpw)

    input_pw.submit

    driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div').click()

    #주피터는 소스코드를 잘라서 실행하기 때문에 종료가 되지 않는다. 하지만 vscode에서는 한번 실행이 되고 작업이 종료되면 driver 기능도 종료되기 때문에 열린 크롬제어창이 닫힌다. 
    #따라서 크롬제어창을 계속 열어두고 싶다면 while 구문을 사용해서 현재 함수가 종료되지 않게 하면 된다. 
    
    while(True):
        pass



login(userid,userpw)

