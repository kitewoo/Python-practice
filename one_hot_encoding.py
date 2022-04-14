#원-핫 인코딩. 데이터의 일치 여부를 1 또는 0 벡터화하는 것.

#모듈 사용 전에 원리 이해하기1
from konlpy.tag import Okt

okt = Okt() # 인스턴스화
tokens = okt.morphs('나는 자연어 처리를 배운다') #형태소 토큰 추출 : okt의 결과 = 나,는,자연어,처리,를,배운다

word_to_index = {word : index for index, word in enumerate(tokens)}
#word_to_index = {}
#for index, word in enumerate(tokens):
#    word_to_index[word] = index

print('단어 집합: ', word_to_index)

def one_hot_encoding(word, word_to_index):
    one_hot_vector = [0]*(len(word_to_index))
    index = word_to_index[word]
    one_hot_vector[index] = 1
    
    return one_hot_vector #word에 해당하는 한 줄의 벡터

for word in word_to_index: #단어 집합 전체 vector
    print(one_hot_encoding(word, word_to_index))
    

#모듈 전에 원리 이해하기2 (pandas)
import pandas as pd

train = pd.DataFrame({'num1': [1,2,3,4,5],
                        'num2': [10,20,30,40,50]
                        ,'cat1': ['a','b','a','c','c']})
print(train)
    #고유값 추출하기
cat_lst = train['cat1'].unique() # 또는 train['cat1'].value_counts().index

    #백터 값 레이블
cat_num = [i for i in enumerate(cat_lst)]

    #원-핫 인코딩

one_h_lst = []

for f in train['cat1']:
    lst=[]
    for i in cat_lst:
        if i == f:
            lst.append(1)
        else:
            lst.append(0)
    one_h_lst.append(lst)

    #벡터화
print(one_h_lst)
    #one-hot-encoding
train_one_df = pd.concat([train, pd.DataFrame(one_h_lst,columns = cat_lst)], axis=1)
print(train_one_df)

    #pandas get_dummies 모듈로 빠르게 벡터화
train_1 = pd.get_dummies(train, columns=['cat1'], prefix='cat1')
print(train_1)

#sklearn으로 원핫인코딩

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse=False) #인스턴스화
train_cat = ohe.fit_transform(train[['cat1']]) #onehotencoder 클래스 내의 fit_transform 모듈은 바로 원핫인코딩해주는 모듈이다.

print(train_cat)



train_cat_df = pd.DataFrame(train_cat, columns=['cat_1'+ cal for cal in ohe.categories_]) #categories_는 원핫인코딩된 unique 값들을 리스트 형태로 리턴한다.

print(train_cat_df)
