import pandas as pd
import numpy as np 

file = pd.read_csv('C:/Users/tt/Desktop/pycode/병합파일.csv')
df = pd.DataFrame(file)

#전국 광역-시군구의 데이터들이 들어있습니다. 
#서울특별시, 부산광역시, 광주광역시, 대구광역시, 울산광역시 추출 -> '지역' 칼럼

list_city = ['서울특별시', '부산광역시', '광주광역시', '대구광역시', ' 울산광역시']
columns = ['지역', '상호', '주소', '상표', '전화번호', '셀프여부', '고급휘발유', '휘발유', '경유', '실내등유']
data = [] 

for c in df.index:
    if df.iloc[c,0] in list_city:
        data.append(df.iloc[c,:])

df_oil = pd.DataFrame(data, columns=columns)

df_oil.reset_index(drop=True, inplace=True)
del df_oil['전화번호']
del df_oil['상호']
del df_oil['고급휘발유']
del df_oil['실내등유']

# 시도별 휘발유의 가격, 셀프여부에 따른 가격 차이도 알고 싶습니다. 

df_oil.info()

## 1. 그 데이터는 영향을 주면 안되니까 제거 
## 2. 평균값을 넣자. 그런데 평균값이 뭐지?
## 3. 결국에는 제거를 하고 제거한 데이터들에서 평균값을 구한 다음에 그 값을 대입하겠습니다. 

df_oil1 = df_oil[(df_oil['휘발유'] != '-') & (df_oil['경유'] != '-')]

df_oil1.reset_index(inplace=True, drop=True)

df_oil1 = df_oil1.astype({'휘발유':int, '경유':int}, copy=True)

print(df_oil1['휘발유'].mean()) #반올림 2002
print(df_oil1['경유'].mean()) #반올림 1919

gas = [] 

for i in df_oil['휘발유']:
    if i == '-':
        gas.append('2002')
    else:
        gas.append(i)

die = []
for i in df_oil['경유']:
    if i == '-':
        die.append('1918')
    else:
        die.append(i)

df_oil['휘발유'] = gas
df_oil['경유'] = die

df_oil = df_oil.astype({'휘발유':int, '경유':int})
print(df_oil.info())

# 데이터 전처리 완료




