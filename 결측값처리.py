#1. 결측값 확인하기 isnull, isna
import pandas as pd

file = pd.read_csv('C:/Users/tt/Desktop/pycode/bank.csv', encoding = 'cp949')

# 행 기준으로 결측값 확인하기
print(file.isnull().any(axis=1)) #axis=1, any는 하나라도 있다면 True 아니면 False

# 열 기준으로 결측값 확인하기
print(file.isnull().any(axis=0)) 

#테이블 전체에서 null 추출. True면 null. 
print(file.isna()) 
print(file.isna().sum()) # 열 기준으로 묶어서 null값 추출. 즉 isnull axis=1 과 동일



#2. 결측값을 어떻게 처리할 지 고민하기
#2-1. 결측값이 있는 데이터는 쓰지 말자고 결정한 경우
    #2-1-1. 행을 삭제하려는 경우 : dropna(how = 'any', 'all', subset=[,]). 별도로 저장해야함.
        #2-1-1-1. how any는 한 개라도 null이면 행 삭제. all은 모두 null이어야 삭제
        #2-1-1-2. subset = ['열 이름'] 으로 특정 열에서 null이 포함되어있는 행 삭제

test_df = file
tdf1 = test_df.dropna(how='any')
print(f'how=any: {tdf1.shape}')

tdf2 = test_df.dropna(how='all') 
print(f'how=all: {tdf2.shape}')

    #2-1-2. 행을 다른 값으로 대체하려는 경우
        #2-1-2-1. 같은 분류의 dtype이 str인 경우 : fillna({"열이름":"unknown"})
bank_df = file.fillna({'contact':'unknown'}) 
print(bank_df.head())   

        #2-1-2-2. 같은 분류의 dtype이 int,float인 경우 
        #평균 등에 활용하려면 0으로 대입해서는 안된다. 아니면 결측값을 제외하고 평균을 구해야 한다. 

        # 결측값 제외하고 평균 계산 : mean()
        # 결측값을 mean()값으로 대체 = fillna()
#bank_df['age'] = bank_df['age'].fillna(mean값)


