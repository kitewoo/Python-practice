# 작업사항 : 서울특별시 공공자전거 대여소 정보를 가지고 원하는대로 시각화하기

from ast import increment_lineno
import matplotlib
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
df1.isna().sum()  #null 값  갯수  열 단위로 확인하기 axis=0이 default, axis=1은 행단위로 null값을 뽑아준다. 

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
plt.bar(df_group.index, df_group['대여소 번호'], color = 'limegreen', label = '대여소 수')

plt.legend()
# 시각화 자료 저장하기
plt.savefig('자치구별 따릉이 대여소 수.png') #현재 작업 경로에 저장된다. show() 전에 둬야한다. show() 소스코드 안에 freed from memory하는 것이 포함되어 있기 때문이다. 

#plt.savefig('name.png', dpi=100, facecolor(배경색)=' ' ,  edgecolor(테두리) = ' ' , linewidth=0, bbox_inches(그래프저장영역)='None,tight', pad_inches(여백)= 0.1,  )

plt.show() #plt.show는 항상 마지막



# pandas.DataFrame.astype({'열이름 : 데이터형식'})  : 특정 열의 dtype을 데이터형식으로 변경하여 표시(카피를 표시하므로 반영하고 싶다면 copy = false 또는 변수로 저장) (특정 열을 지정하지 않고 데이터형식만 입력하면 전체가 다 바뀜) , copy = false로 넣으면 porpagate될 수 있다.
# pandas.DataFrame.unique() : 고유값 추출하여 리스트 형태로 출력 
# pandas.DataFrame.nunique() : 고유값 종류 갯수
# pandas.DataFrame.value_counts() : 고유값별로 데이터의 수 출력, 내림차순이 default. 오름차순으로 보고싶다면 () 안에 ascending = True 입력
# pandas.DataFrame.insert(columns index, '열 이름', value(scalar,series,array), allow_duplicates = False) : 열 인덱스에 해당하는 곳에 '열 이름'으로 열 삽입. 원래 있던 열부터 오른쪽으로 한칸씩 이동
# pandas.DataFrame.rename(columns = {'a':'b'}, inplace = True) : 열이름 a를 b로 변경하고 저장
# pandas.DataFrame.drop(['열이름'], axis=1, inplace=True) : 특정 열 제거



# 데이터 분포 보기(히스토그램) 

bank_df = pd.read_csv('C:/Users/tt/Desktop/pycode/bank.csv', encoding = 'cp949')

plt.hist(bank_df['age'])
plt.xlabel('age')
plt.ylabel('frequency')
plt.show()

# 두 열을 기준으로 산포도 작성
plt.scatter(bank_df['age'], bank_df['balance'])
plt.xlabel('age')
plt.ylabel('balance')
plt.show()

# 상관계수 계산
print(bank_df[['age','balance']].corr())  #나이와 자산의 상관계수는 0.11236으로 낮다.

# 산포도행렬의 작성
pd.plotting.scatter_matrix(bank_df[['age','balance','day','duration']])
plt.tight_layout()
plt.show()

# pie chart : 비율 차트
job_u = bank_df['job'].unique()
    #비율 계산 2가지 방법
    #1. bank_df.groupby('job')[['age']].count()/len(bank_df))
    #2. bank_df['job'].value_counts(ascending=False, normalize=True) : Return a 'Series' containing counts of unique values.
job_ratio = bank_df['job'].value_counts(normalize=True, ascending=False)#If True then the object returned will contain the relative frequencies of the unique values.

plt.pie(job_ratio, labels=job_ratio.index)
plt.show()

