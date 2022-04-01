# 작업사항 : 서울특별시 공공자전거 대여소 정보를 가지고 원하는대로 시각화하기

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
from matplotlib import rc_params

#1. 파일 불러오기
file_path = "C:/Users/tt/Desktop/pycode/공공자전거 대여소 정보(21.12월 기준).csv"

df = pd.read_csv(file_path, encoding='cp949', header=4)

#확인해본 결과 5행부터 유효한 값이 있음. 따라서 header 수정했음.

#만약 불러올 데이터가 여러개라면?

#import glob
#path = ' '
#files = glob.glob(path + '*자전거*.csv')

#2. 데이터 전처리

#2-1. 필요한 데이터는 '대여소 번호', '보관소(대여소)명', '자치구', '주소', '위도', '경도' . 나머지는 삭제

df1 = df.iloc[:,0:6] #필요한 것만 선택하여 저장. (또는 del df['']로 지울 수 있음)

df1.columns = ['대여소 번호', '보관소(대여소)명', '자치구', '주소', '위도', '경도'] #열 이름 지정

df1.info()  
df1.isna().sum()  #null 값  갯수 확인하기

# 만약 Nan값이 있다면? 1. 행or열 전체 삭제 2. null값 대체 
# 1. 전체 삭제는 pd.DataFrame.dropna()
    ## axis = 0 이면 행 삭제, axis = 1 이면 열 삭제
    ## how = any 이면 null값이 하나라도 있으면 삭제. how = all 이면 모두 null 값이어야 삭제
    ## thresh = int : 축(axis)을 기준으로 값이 n개 미만으로 입력되면 그 축을 삭제한다. 
    ## inplace = False가 default. 따라서 삭제를 반영하려면 inplace=True
    ## subset = ['열이름'] : 해당 열의 null만 고려하여 삭제

# 2. 대체 pd.DataFrame.fillna()
    ## 대체 가능한 값(value) : scalar, dict(key, value), Series, DataFrame
    ## method = bfill(바로 행 아래 값과 동일하게 대체), ffill(위 값과 동일)
    ## limit = int : method가 정해진 경우 최대값을 설정
    ## axis : 0 or index (행 대체) , 1 or columns (열 대체)
    

# 자치구별 대여소 수가 궁금하다. 

    # pandas groupby 사용하기
    # groupby('기준 열이름') -> 기준 열이름이 행 index가 되면서 다른 열들이 DataFrame으로 묶인다. 
    # 특정 대상만을 묶고 싶다면 groupby('기준 열이름')[['묶을 대상']]을 하면 된다. 
    # groupby('기준 열이름')[['묶을 대상']].sum() .mean() 등 가능

df_group = df1.groupby('자치구')[['대여소 번호']].sum()

print(df_group)

# 시각화하기

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(15,10))
plt.title('자치구별 따릉이 대여소 수')
plt.bar(df_group.index, df_group['대여소 번호'], color = 'limegreen')
plt.legend
plt.show()










