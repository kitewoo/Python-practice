import pandas as pd 

# 아나콘다란? 파이썬 언어와 파이썬을 입력하고 실행하기에 필요한 툴 그리고 주요 라이브러리 패키지.
# 주피터 노트북이란? 파이썬을 웹 브라우저 내에서 입력하고 실행할 수 있는 툴. 장점은 코드 전체를 실행하는 것이 아니라 중간에 필요한 부분만 실행해볼 수 있어서 학습에 유용하다. 

# 파이썬 기초
    #파이썬 사칙연산 중 기억에 안남아서 나를 귀찮게 하는 것 : a//b는 a를 b로 나누었을 때 몫. a%b는 a를 b로 나누었을 때 나머지.
    
    #print로 출력할 때 값들 사이 구분 기호는 default가 띄어쓰기이고 특정 기호를 넣고 싶을 때 sep라는 parameter를 사용하면 된다. 


print("BTCUSDT", "SANDUSDT", "LRCUSDT") #이렇게하면 띄어쓰기로 구분된다.

print("BTCUSDT", "SANDUSDT", "LRCUSDT", sep = '/') 

# 파이썬의 자료형

## int (정수형)
    ### 만약 연산을 해야할 상황이라면 그 데이터는 int or float형이어야 한다. 만약 데이터가 str이라면 typeerror가 발생할 수 있다. 따라서 str을 int로 바꿔주는 일은 빈번하다. 
    ### 하나의 변수를 숫자로 변경하려면? int() 함수를 사용

a = "123" #str로 변수 저장

print(type(int(a)))  #int로 출력된다. 

## float (실수형)

## str (문자열)
'' "" ''' ''' '이런 작은따옴표, 큰따옴표 사이에 넣으면 된다.'


## dictionary (딕셔너리형) : "key" : "value" 구조 리스트처럼 KEY를 부르면 VALUE가 나옴
dic1 = {"name":"kakao", "phone":"010-1234-1234", "address":"Seoul"} 
print(dic1["name"])
    ### dic의 key는 고유값이기 때문에 2개 이상이 되면 마지막 것만 살고 나머지는 무시된다. 
    ### key에 리스트를 사용할 수 없다. 
    ### tuple은 key로 사용할 수 있다. 
    ### key로 dic을 사용할 수 없다. 

    ### keys 매서드 : 키 값을 리스트로 return 
print(dic1.keys())

dict2={"번호":[1,2,3,4,5],
       "이름":["AAA","BBB","CCC","DDD","EEE"],
       "성별":["남","여","남","여","남"],
       "점수":[100,90,90,80,70]}

df2=pd.DataFrame(dict2) #key값이 column 값으로 들어감. 딕셔너리 value 갯수들이 같아야 한다. 
print(df2)

## list (리스트형)
a = ['a','b','c',1,2,3,[1,2],[3,4]] #이처럼 str, int, float, list, tuple,dic 등 모든 자료형을 담을 수 있다. index는 0부터 시작한다. 
    ### index하는 법

a[0] #개별 인덱싱
a[0:3] #0부터 2까지 범위 인덱싱
a[-1] #뒤에서 첫번째 인덱싱
a[6][0] #2차원 인덱싱
    ### 리스트 병합 방법 1 : 현 리스트에 뒤로 요소들로 추가 

b = [1,2,3]
c = [3,4,5]

print(b+c) #순차적으로 리스트를 합친다. b 뒤에 c를 더한다 
print(b) #위의 합은 지역변수로 남아있어서 b와 c 자체를 바꾸지는 않았다. 

        #반복문에서 활용하기 : 비어있는 리스트 list=[]에 새 요소들을 계속 넣어주려면 list += list + 변수 로 하면 된다. 

    ### 리스트 병합 방법 2 : append 함수로 마지막에 요소 하나로 추가
b.append(c) # b에 리스트c가 바로 요소로 들어가고 저장되어 전역변수가 된다. 별도로 변수로 저장할 필요는 없다. 

        #반복문에서 활용하기 : 리스트가 아닌 일반 정수형이면 이것으로 해도 된다. 하지만 리스트를 추가하는 경우에는 요소별로 뿌려주지 않기 때문에 n차원으로 접근해야하는 문제가 생긴다. 

print(b)

    ### 리스트와 pandas DataFrame 
list = [[1, '이재명', '남성'], [2, '윤석열', '남성'], [3, '심상정', '여성']] #이렇게 동일한 개수의 요소들로 이루어진 2차원 리스트는 df로 변경할 수 있다.

df1 = pd.DataFrame(list, columns = ['기호','후보','성별']) #이렇게 요소의 갯수와 컬럼의 갯수를 일치시키면 된다. 
print(df1)

## tuple (튜플형) : 리스트와 달리 그 값의 생성, 삭제, 수정이 불가능하다.  -> typeError 발생
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1+tuple2)


## 집합 : set 키워드를 이용해 만들어지는 자료형. 중복 허용X, 순서가 없음. 따라서 집합을 인덱싱으로 접근하려면 리스트나 튜플로 변환해야 한다. 
s1 = set([1,2,3])
s2 = set("hello")
#s3 = set(1,2,3) 숫자를 여러개 넣을 때에는 리스트 구조형을 갖추어야 한다. 

# l1 = list(s1) #리스트 구조를 갖추고 있는 자료형을 list 자료형으로 변환 : 2차원으로 나올 줄 알았는데 그냥 에러뜸
#l3 = list(s3) #이렇게 리스트 구조를 갖추고 있지 않으면 typeError가 발생한다.
l2 = tuple(s2)

    ###교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1&s2)

    ###합집합
print(s1|s2)
print(s1.union(s2))

    ###차집합
print(s1.difference(s2))

    ###집합에 요소 하나 추가
#print(s1.add(4)) #이 상태에서는 아직 지역 변수다
#s1 = s1.add(7)
#print(s1) #??? 왜 None이 나오지?

    ###집합에 요소 여러 개 추가
#s1.update([8,9,10])
#print(s1) #이건 또 왜 없다고 하지?

    ### 특정 값 제거
#s1.remove(2)
#print(s1) 엥 이것도 안되는데?

## bool 자료형 : True, False
print(bool("python"))
print(bool(""))

#변수 : 프로그램 내에서 계산시 사용할 일부 값을 저장하는 예약된 메모리
    ##변수로 선언할 수 있는 형태 : 문자(대소문자 구분), 숫자, 언더바(_). 나머지는 사용할 수 없다. 
    ##예약어는 변수로 사용할 수 없다. 
    ##변수의 첫째 자리에서는 숫자를 사용할 수 없다. 

    ##변수.count(값) : 변수 안에 값을 포함하는 개수가 몇 개인지 세는 함수
str1 = "문자 숫자 리스트 문자열 텍스트 정수형"
print(str1.count("문자")) 
#



#pandas DataFrame 데이터 형식 변경 : astype모듈 

#DataFrame.astype(dtype, copy=True, errors='raise') 
#copy는 default가 True이다. 만약 False로 바꾸면 원본 데이터 객체에 저장된다.
#errors의 default는 raise이다. 여러 개를 대체할 때 하나라도 대체할 수 없을 때 error가 뜨는데 그것을 무시하고 변경하려면 'ignore'로 바꾸면 된다.

col1 = [1,2,3,4] #int
col2 = ['1', '2', '3', '4'] #str
col3 = ['1', 'r', 'b' , '4'] #str
df = pd.DataFrame(data={'col1':col1, 'col2':col2, 'col3':col3})

# 1. 특정 열만 바꾸기

# df.astype({'col2':'int', 'col3':'int'}, copy=True, errors='raise') #에러 발생 : col3에서 int로 바꿀 수 없는 요소가 있기 때문
df = df.astype({'col2': 'int64' , 'col3': 'int32' }, errors='ignore') 

# 바꾸려고 하는 데이터형식을 입력하는 방법은 그냥 int 이렇게 입력해도 되고 str로 'int' 이렇게 입력하면 된다. 그냥 입력하면 자동으로 맞는 int로 바꿔준다. int32, int64를 특별히 지정해주고 싶다면 str로 작성해야 한다. 

print(df.info())


# 모든 열을 다 바꾸고 싶으면 df.astype(dtype='int') 이런 식으로 입력하면 된다. 
