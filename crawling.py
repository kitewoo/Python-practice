from importlib.resources import path
from re import X
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from datetime import datetime 
from datetime import date
from datetime import timedelta

#requests 라이브러리 : HTTP, HTTPS 웹 사이트에 소스코드를 요청. (요청 method : get, post)
#BeautifulSoup : HTML과 XML 파일에서 데이터를 뽑아내기 위한 파이썬 라이브러리. 트리 구조를 탐색,검색,변경 가능하다. 4 종류의 parser(컴파일러의 구성 요소로 일련의 문자열을 토큰 단위로 분해하고 트리를 만드는 과정)를 제공

#BeautifulSoup 모듈 사용법 
# 1-1 . BeautifulSoup(markup, 'html.parser') 설치 없이 바로 html 문서를 parsing. 대부분 1번이다.
# 1-2. XML인 경우 lxml을 추가 설치하여 (markup, 'xml)로 사용 

# 2-1. 태그 검색 : find() , find_all(), select()
# find() : 해당 조건에 맞는 첫 번째 태그를 검색
# find_all() : 해당 조건에 맞는 모든 태그를 검색하여 list 형태로 도출
# select() : CSS 선택자와 같은 형식으로 선택 가능 -> f12(개발자도구) 우클릭 > copy > copy selector

    ## STEP 0 : 추출할 날짜 데이터 정리하기 
today = date.today()
num_day = 100
datelist = [(today - timedelta(days=i+1)).strftime('%Y%m%d') for i in range(0,num_day)] #int들이 들어있는 리스트

#datelist = list(map(str, datelist))

print(datelist)

#for i in range(0,num_day):
#    datelist.append(today - datetime.timedelta(days=i))
#한줄쓰기

#today = str(today.year)+str(today.month)+str(today.day)

    ## STEP 1 : Parsing 하기 

bugs_day = [] 

for x in datelist:
    url = "https://music.bugs.co.kr/chart/track/day/total?chartdate=" #벅스뮤직 일일 차트
    url = url + x
    html = requests.get(url)
    soup = bs(html.text, "html.parser") 

    #print(soup) #html을 가져온 것을 확인할 수 있다.
    #웹사이트를 보면 알겠지만 일일 차트의 열 이름은 다음과 같다. ['순위','곡','아티스트','앨범'] 
    #html 구조를 보면 tbody > tr > td > p > a  tbody > tr > div 등으로 이루어져 있다. tbody가 전체 테이블을 가르키고 있다. 이를 하나씩 소환하면 된다. 
    #순위는 tbody > tr > div class_ranking
    #곡은 tbody > tr > th > p class_title
    #아티스트는 tbody > tr > td > p class_artist > a href 에 있다. 
    #앨범은 tbody > tr > td > a class_album 에 있다. 

    # 순위1 열 데이터를 가져와 보자 
    #bugs_day = []

    tbody = soup.find("tbody") #공통분모 1 
    tr_soup = tbody.find_all("tr") #공통분모 2, tbody 안에는 1위부터 100위까지가 각각 묶여있다. 여러 개가 있으니 find all

    #rank = tr_soup[0].find("div", class_='ranking').get_text().split('\n')[1]
    #title = tr_soup[0].find("p", class_='title').get_text().replace('\n','')
    #artist = tr_soup[0].find("p", class_='artist').get_text().replace('\n','')
    #album = tr_soup[0].find("a", class_='album').get_text().replace('\n','')

    #bugs_day.append([rank, title, artist, album])

#print(bugs_day)

#그럼 이걸 반복하면 오늘의 1위부터 100위까지를 뽑아서 excel 파일로 저장할 수 있을 것이다. 

    for i in range(len(tr_soup)):
        day = x
        rank = tr_soup[i].find("div", class_='ranking').get_text().split('\n')[1]
        title = tr_soup[i].find("p", class_='title').get_text().replace('\n','')
        artist = tr_soup[i].find("p", class_='artist').get_text().replace('\n','')
        album = tr_soup[i].find("a", class_='album').get_text().replace('\n','')

        bugs_day.append([day, rank, title, artist, album])

#결과 : bugs_day에 1위부터 100위까지 2차원 리스트가 만들어질 것
#DataFrame으로 변환

df_rank = pd.DataFrame(bugs_day, columns=['일시','순위','곡','아티스트','앨범'] )

#print(df_rank.head())
#df_rank.to_excel("C:/Users/tt/Desktop/pycode/bugs_chart_20220325.xlsx", sheet_name='new_name', index='False')

# 시각화하기 (100일분)
## 1위만 누적 데이터를 구해보자
df_rank1 = df_rank[df_rank['순위']=='1']
df_rank1 = df_rank1.groupby('아티스트')[['곡']].count() #정렬 : ascending = False (내림차순) True(오름차순)
print(df_rank1.head())

# 어떤 아티스트가 최근 100일간 1위를 가장 많이했을까?
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(20,15))
plt.title('최근 100일간 1위를 기록한 아티스트 (누적)')
plt.style.use('ggplot')
plt.xticks(size=9, rotation = 45)
plt.ylabel('1위 횟수')
plt.bar(df_rank1.index, df_rank1['곡'], color = 'coral', label = '1위 횟수')

plt.legend()
plt.savefig('벅스뮤직 일간 차트 최근 100일 누적 1위 아티스트')
plt.show()

##