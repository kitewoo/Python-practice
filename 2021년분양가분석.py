import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

housing_df = pd.read_csv('C:/Users/tt/Desktop/pycode/house_price_preprocessing_2021.csv', encoding='cp949', thousands=',')
#열 이름 변경
housing_df.rename(columns = {'분양가격(제곱미터)':'분양가격'}, inplace=True)
housing_df.info()

housing_df.dtypes
housing_df.isna().sum()

#분양가격에 결측치 있음

housing_df = housing_df.fillna({'분양가격': 0})
housing_df['분양가격'].isna().sum()

housing_df = housing_df.astype({'분양가격': 'str'})

price_int = housing_df['분양가격'].apply(lambda x: x.replace(',',''))
price_int.tail()

del housing_df['분양가격']

housing_df = pd.concat([housing_df, price_int], axis=1)
housing_df.replace('-','')

idx = []
for i in housing_df.index:
    if housing_df.iloc[i,4] == '0':
        idx.append(i)
        
len(idx)

house_df = housing_df.drop(idx,axis=0)
    
house_df.count()

house_df.loc[:10, ['분양가격']]

price = [] 

for p in house_df.index:
    if house_df.loc[p,'분양가격'] == '  ':
        house_df.drop(p, axis=0, inplace=True)

house_df.info()

for p in house_df['분양가격']:
    if p == '  ':
        price.append(p)

house_df = house_df.astype({'분양가격':int})
house_df['분양가격'] = house_df['분양가격']/3.3
house_df.head()


# 그래프 출력 시 이상한 에러들 무시
import warnings
warnings.filterwarnings("ignore")

# 그래프 그릴 때 한글 깨짐 방지 설정
import os

# Mac OS의 경우와 그 외 OS의 경우로 나누어 설정
if os.name == 'posix':
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")

average_df = house_df.groupby('지역명')['분양가격'].mean()

# groupby()를 이용해 '지역명'으로 묶어 count 구하기

average_df.count()

sns.barplot(x = average_df.index, y=average_df)

plt.show()

# 지역명을 기준으로 평당분양가격의 중위값 계산
# aggfunc 옵션에 np.max를 입력하여 최대값 데이터를 출력
# pivot_table로 데이터 분석(기본적 평균값 출력)

pd.pivot_table(house_df, index=['지역명'],values=['분양가격'], aggfunc=['mean','var','min','max','median'])

# 지역별/연도별 평당분약가격 평균 계산

pd.pivot_table(house_df, index=['지역명','연도'],values=['분양가격'], aggfunc=['mean','var','min','max','median'])