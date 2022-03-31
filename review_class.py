#객체 지향 프로그래밍의 꽃 Class
#class는 데이터 형식의 하나. 이게 파일이 되면 그 파일을 모듈이라고 부른다. 
 
#슈퍼마리오 게임을 만든다고 가정하자. 

pos = 0 #슈퍼마리오의 초기 위치

def forward(pos):
    return pos + 20

pos = forward(pos)

print(pos)

#이걸 매일 새로 써야한다고 하면 참 귀찮다. 그래서 하나의 객체로 만들어놓고 그 객체를 불러와보자.

class SuperMario:
    def __init__(self):
        self.pos = 0
    
    def forward(self):
        self.pos = self.pos + 20 #클래스는 함수와 데이터로 이루어져 있다. 
    

mario = SuperMario()
mario.forward()

print(mario.pos)

# 자 이제 class가 왜 효율적인지 알 수 있다.
mario_p1 = SuperMario()
mario_p2 = SuperMario()

mario_p1.forward() #forward 함수 1회 실행
mario_p1.forward() #forward 함수 2회 실행 init이랑은 분리가 되어있기 때문에 0으로 초기화되지 않는다. 

print(mario_p1) #이렇게하면 main이 출력이 된다. 왜냐하면 클래스 자체를 출력하라고 했기 때문이다. 즉, 그 안에 무엇인가를 불러야 한다. 

print(mario_p1.pos)
print(mario_p2.pos)




