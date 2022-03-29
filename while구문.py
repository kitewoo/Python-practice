#while + 조건문 : 
#       조건에 맞으면 실행할 문장1
#       조건에 맞으면 실행할 문장2

#따라서 조건에 안맞으면(False) 반복할 문장들을 빠져나가게 된다. 

from sympy import true


#prompt = """ 1.Add 2.Del 3.List 4.Quit Enter Number: """

#number = 0
#while number != 4:
#    print(prompt)
#    number = int(input())

#여기서 4를 input하기 전까지 계속 반복된다. 즉, while은 무한반복문이다. 
#참이기만 하면 계속 돈다.

#그렇다면 조건문이 계속 True일 때 그 도르마무를 끝내기 위해서는 어떻게 해야할까? (참 거짓이 없으면 참이 default)

dormamu = 0
stranger = true
while stranger:
    print("도르마무!! 거래를 하러 왔다!")
    dormamu = int(input("3번의 기회를 주지, 비밀번호를 풀어라: "))
    if dormamu == 3 :
        break 


#while문을 진행하던 중에 while 조건문이 아니라 중간에 조건문을 넣어 처음으로 다시 돌아가고 싶은 경우에는 continue를 활용하면 된다.

a = 0
while a<10 :
    a = a+1
    if a % 2 == 0 : continue
    print(a)

# 무한 루프를 사용하려면 while True:를 사용하면 된다. Ctrl + C 를 누르면 빠져나갈 수있다. 

while true:
    print("Ctrl+c를 눌러야 while 무한 루프에서 빠져나갈 수 있습니다.")
    

