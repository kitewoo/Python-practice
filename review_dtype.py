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


## tuple (튜플형) : 리스트와 달리 그 값의 생성, 삭제, 수정이 불가능하다.  -> typeError 발생
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1+tuple2)

## 집합 

