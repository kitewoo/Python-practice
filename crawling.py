from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from datetime import datetime 

#BeautifulSoup : HTML과 XML 파일에서 데이터를 뽑아내기 위한 파이썬 라이브러리. 트리 구조를 탐색,검색,변경 가능하다. 4 종류의 parser(컴파일러의 구성 요소로 일련의 문자열을 토큰 단위로 분해하고 트리를 만드는 과정)를 제공

#BeautifulSoup 모듈 사용법 
# 1-1 . BeautifulSoup(markup, 'html.parser') 설치 없이 바로 html 문서를 parsing. 대부분 1번이다.
# 1-2. XML인 경우 lxml을 추가 설치하여 (markup, 'xml)로 사용 

# 2-1. 태그 검색 : find() , find_all(), select()
# find() : 해당 조건에 맞는 첫 번째 태그를 검색
# find_all() : 해당 조건에 맞는 모든 태그를 검색하여 list 형태로 도출
# select() : CSS 선택자와 같은 형식으로 선택 가능


    ## STEP 1 : Parsing 하기 

url = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
url = url + str("20220323")
