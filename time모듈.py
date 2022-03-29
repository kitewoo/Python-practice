#time모듈

#참조: https://wikidocs.net/33
#time -time.time(): UTC(런던 기준시) 현재 시간을 실수 형태로 출력 (1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.)

#time.localtime():년,월,일,시... 출력

import time

stime=time.time()

print(time.time())
print(time.localtime(time.time()))
print(time.strftime("%c", time.localtime(time.time()))) #ftime은 시간을 문자(str)로 바꾸는 것
print(time.strftime("%x", time.localtime(time.time())))

#print(time.strptime) #시간 데이터로 바꾸는 것

tot = 0
for i in range(10):
    time.sleep(1) # 1초 대기 명령
    tot += tot + i 

print(tot)

print(time.time() - stime) #코드 종료시간 - 시작시간 (즉, 코드 실행 시간)

#os 모듈
#os.mkdir(folder_name) : 현재 작업경로에 폴더 만들기
#os.mkdir(os.getcwd()+"/하위폴더/"+folder_name)#