from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import alert
import requests
import time
from tqdm import tqdm
from konlpy.tag import Okt
import re
from collections import Counter

driver = webdriver.Chrome("C:/Users/tt/Desktop/pycode/chromedriver.exe")

url = 'https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=%EA%B3%A0%EC%96%91%EC%9D%B4+%EC%B8%84%EB%A5%B4'
driver.get(url)

for i in range(6):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)

html = driver.page_source
soup = bs(html, 'html.parser')

text1 = soup.find_all('div', class_='basicList_title__3P9Q7')
text2 = [] 

for text in text1:
    title = text.find('a', target='_blank').get_text()
    text2.append(title)

for x in range(20):

    for i in range(6):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    html = driver.page_source
    soup = bs(html, 'html.parser')

    text1 = soup.find_all('div', class_='basicList_title__3P9Q7') 

    for text in text1:
        title = text.find('a', target='_blank').get_text()
        text2.append(title)
    
    try: 
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[3]/div/a['+str(x+1)+']')))
        
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[3]/div/a['+str(x+1)+']').click()

    except:
       print("페이지를 시간 내에 로드하지 못했습니다.")
    
okt = Okt() #클래스를 인스턴스화
nouns = []
stopword = ['고양이','츄르','간식','대','용량','짜','먹는','개입','스틱','개','맛']

for text in text2:

    reg_text = re.sub(r'[0-9a-zA-Z]+','',text)
    reg_text = re.sub(r'[-!:(;)+-/\.,\-![]]',"",reg_text)
    reg_text = re.sub(r'[-()/+=&]',"", reg_text)

    words = okt.morphs(reg_text) #형태소 기준으로 추출
    for i in words:
        if i not in words:
            nouns.append(i)

cnt = Counter(nouns)

wordinfo = dict()
for x,y in cnt.most_common(150): #상위 150개 # 그냥 Counter로 뽑으면 리스트화 할 수 가 없음.. 이건 복잡해서 다음에
    wordinfo[x]=y

dict_df=pd.DataFrame(wordinfo, index=[0])

dict_df.to_excel('고양이츄르.xlsx')




    
