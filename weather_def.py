# 필요한 모듈 연결하기
from datetime import datetime, timedelta
import json
import pandas as pd
import requests

#시작일 입력 함수

def startdate():
    while True:
        startday = input("시작일을 입력하세요: 예)2022-01-01: ")
        
        if len(startday) != 10:
            print("20yy-mm-dd 형식으로 입력하세요.")
            continue
            
        try:
            sdt = int(startday.replace("-",""))
            break
            
        except:
            print("년, 월, 일 자리에 문자가 포함되어 있습니다. \n 숫자로 다시 입력해주세요.")
            
            continue
        
    return sdt


#시작일, 종료일 입력 받는 함수
def endDate():
    sdt=startdate() #시작일 입력 받기
    
    while True:
        endday = input("종료일을 입력하세요: 예)2022-01-01: ")
        
        if len(endday) != 10:
            print("20yy-mm-dd 형식으로 입력하세요.")
            continue
        
        # "-"를 뺀 나머지 입력 ㄷ이터가 모두 숫자인지 아닌지 확인
        # 문자 포함시 다시 입력받기
        # 입력한 종료일이 오늘 날짜인지 확인/ 오늘날짜-1 한 날짜로 세팅
             #today = datetime.today() #현재 시스템 날짜를 가져오기
            #newdate = today.strftime("%Y%m%d") #strftime : 날짜/시간을 str로 변환
        
        try:
        # 입력한 종료일이 시작일보다 크거나 같은 값인지 확인 -> 재입력
            edt = int(endday.replace("-",""))
            today = datetime.today()
            newdate = today.strftime('%Y%m%d')
        
            if edt >= int(newdate):
                #크거나 같다면 실행 전날로 종료일 변경
                endday = (datetime.today()-timedelta(day=1)).strftime("%Y-%m-%d")
                print('데이터는 당일 이전 자료까지만 제공합니다.')
            
            if sdt > edt:
                print("종료일이 시작일보다 이전 날짜입니다. \n 다시 입력해주세요.")
                continue

            break
        
        except:
            print("년, 월, 일 자리에 문자가 포함되어 있습니다. \n숫자로 다시 입력해주세요.")
            
            continue
       
    
    return sdt, edt

#지점 코드
def getregcode(inregname='서울'):
    
    df_regcode = pd.read_csv("C:/Users/tt/Desktop/pycode/기상청_지역코드.csv")
    #df_regcode[df_regCode['지점명']=='속초']
    df_regcode = df_regcode[['지점','지점명','관리관서']]
    df_regcode

    regcode = df_regcode[df_regcode['지점명']==inregname]

    if len(regcode) == 1:
        return int(regcode['지점'].values)

    else:
        # 검색 자료가 없으면 강제로 에러가 나오게 하는 함수
        raise Exception(f"해당 지역명은 없습니다.")


import json

def weather_url(sdt, edt, pointID, rows=31):
    
    key = "gUrvbzp3W5b7phwzfxKiQ6xKhRvmc5zRLfM1BZiL4uwfBOHMRkEc8EmX%2Bbno7S8NHSlOsm0QfwMQisDlM9kzXQ%3D%3D"
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey="
    url = url + key
    url = url + "&numOfRows=" + str(rows)
    url = url + "&pageNo=1&dataCd=ASOS&dateCd=DAY&dataType=JSON&startDt=" + str(sdt) #datatype = JSON
    url = url + "&endDt=" + str(edt)
    url = url + "&stnIds=" + str(pointID)
    
    return url

def getJsonData(url):
    soup_json=requests.get(url)
    if soup_json.status_code != 200:
        exit(f"데이터를 받지 못했습니다. 에러코드 : {soup_json.status_code}")
    json_obj = json.loads(soup_json.text) #json 코드 읽어오기/딕셔너리 구조
    
    return json_obj

def getDataFrame(sdt,edt,pointID):
    url=weather_url(sdt, edt, pointID) # 1차 url 생성
    json_obj=getJsonData(url)
    numRows = json_obj["response"]["body"]["totalCount"] #조회 데이터 건수
    
    url=weather_url(sdt, edt , pointID, numRows) # url 생성
    json_obj=getJsonData(url)   # 최종 데이터 추출
    items=json_obj["response"]["body"]["items"]['item'] # 필요한 item 값만 가져오기
    df1=pd.DataFrame(items)  # items(딕셔너리 구조)를 DataFrame으로 변경
    
    df1=df1[['stnNm', "tm", "avgTa", "minTa", "maxTa", 'sumRn']] # 원하는 열만 추출
    
    return df1

sdt, edt = endDate()
pointName = input("지점명 입력: ")
pointID=getregcode(pointName)

df1=getDataFrame(sdt, edt, pointID)

df1.info()

