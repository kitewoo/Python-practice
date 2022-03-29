# selenium은 웹사이트 테스트를 위해 만들어진 도구 : 코딩으로 동작을 제어할 수 있다. (클릭, 로그인 등)
# selenium을 사용하려면 webdriver를 웹브라우저 버전에 맞게(앞 두자리) 설치해야 한다. 크롬을 사용하는 경우 chromium을 사용할 수 도 있다. 

from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time
import pandas as pd

driver=webdriver.Chrome("C:/Users/tt/Desktop/pycode/chromedriver.exe") #크롬드라이버 실행 객체 

url="https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword=국내 여행지"
driver.get(url) #변수 url에 저장된 웹 주소로 접속
time.sleep(2)

html=driver.page_source #html의 정보 가져오는 모듈
soup=BS(html, "html.parser") #html의 정보들을 parsing 

post_soup=soup.find_all("div", class_="list_search_post") #찾고자 하는 정보들이 div 태그와 class "list_search_post"라는 속성으로 규칙적으로 묶여있음을 확인했고 그것을 모두 찾는 것. 리스트 형태로 저장
#print(post_soup[0].find("strong",class_="title_post").get_text()) #위 리스트 중 첫 번째 요소에서 strong 태그와 class "title_post"에 제목이 들어가있음을 확인. 그 텍스트를 가져온다. 
#print(post_soup[0].find("a")["href"]) #해당 게시글의 link는 a태그의 href 속성에 담겨있다. 이 자료는 div > a * href 이다. 따라서 2차원 배열 

# 반복문을 통해 해당 페이지의 정보 반복하여 가져오기
#
post_soup=soup.find_all("div", class_="list_search_post")
post_list=[]
for post in post_soup:
    title=post.find("strong",class_="title_post").get_text().replace("\n","") #find("태그", 하위태그)
    href=post.find("a")["href"] #(태그)[속성명]
    post_list.append({"제목":title, "링크":href}) #딕셔너리로 리스트에 요소들을 추가

#print(post_list)
df=pd.DataFrame(post_list)
print(df)


#위의 과정을 결과 검색창 내에서 표현된 블로그 글의 제목과 요약 내용들을 볼 수 있었다. 여기서 그 글 전체 내용을 가지고 오고 싶다면 해당 링크로 들어가서 세부 주소를 가져와야 한다. 

blog_link = []
for i in df.index:
    
    driver.get(df.loc[i, "링크"])
    time.sleep(2)

    html=driver.page_source
    soup=BS(html, "html.parser")
    blog_link.append(str("http://blog.naver.com"+ soup.find("iframe", id="mainFrame")['src']))


#게시글의 내용 가져오기
import requests
for link in blog_link:
    html = requests.get(str(link))
    soup = BS(html.text, "html.parser")
    text = soup.find("div", class_="se-main-container").get_text()
    print(text)
 
