from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import alert
import requests
import pandas as pd
import time
from tqdm import tqdm

driver = webdriver.Chrome("C:/Users/tt/Desktop/pycode/chromedriver.exe") # 크롬 드라이버 실행

url = "https://www.opinet.co.kr/searRgSelect.do"
driver.get(url)


try: 
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="header"]/div/ul/li[1]/a')))

except:
    print("페이지를 시간 내에 로드하지 못했습니다.")


driver.find_element(By.XPATH, '//*[@id="header"]/div/ul/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="header"]/div/ul/li[1]/ul/li[1]/a').click()

try: 
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="searrgVO"]/div[1]')))

except:
    print("페이지를 시간 내에 로드하지 못했습니다.")

html = driver.page_source
soup = bs(html, 'html.parser')
search = soup.find('dd', class_='fir')
option = search.select_one('#SIDO_NM0')

opsido = []
options = list(option)
for op in options:
    if op != '\n':
        opsido.append(op)

del opsido[0]

for i in range(len(opsido)):
    
    driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]/option['+f'{i+2}'+']').click()
    
    html = driver.page_source
    soup = bs(html, 'html.parser')
    search = soup.find('dd', class_='fir')
    SIGNGU_options = search.select_one('#SIGUNGU_NM0')
    opsigungu = []   
    sioptions = list(SIGNGU_options)
    
    for sop in sioptions :
        if sop != '\n':
            opsigungu.append(sop)
    del opsigungu[0]
    
    for j in range(len(opsigungu)): 
        driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]/option['+f'{i+2}'+']').click()
        try:
            driver.find_element(By.XPATH, '//*[@id="SIGUNGU_NM0"]/option['+f'{j+2}'+']').click()
   

            time.sleep(0.3)
    
            driver.find_element(By.XPATH,'//*[@id="templ_list0"]/div[7]/div').click()
        except:
            pass

        

import glob

file_format = ".xls"
file_path = 'C:/Users/tt/Desktop/pycode/주유소 데이터'
file_list = glob.glob(f'{file_path}/*{file_format}') #파일 형식과 파일 경로 포함하는 것들을 모두 리스트로 저장

merge_df = pd.DataFrame()

for file_name in file_list:
    file_df =pd.read_excel(file_name, header = 2)
    columns = list(file_df.columns)
    temp_df = pd.DataFrame(file_df, columns=columns)
    merge_df = merge_df.append(temp_df, ignore_index = False)


merge_df.to_csv("병합파일.csv", index=False)


data = pd.read_csv('병합파일.csv')
print(data.head())
print(data.tail())
