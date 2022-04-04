# Python TIL(today I learned) 입니다. 
> 파이썬을 통해 배운 것들을 기록했습니다.

## dtype

## for 구문

## while 구문

## def 

## bs4 
> bs4는 requests된 웹브라우저의 html 정보를 가져와서 parsing하고 그 안에서 값들을 검색, 추출하는 라이브러리이다. 
 ### bs4의 하위 패키지 BeautifulSoup : from bs4 import BeautifulSoup as bs
> #### 1. bs(html, 'html.parser)
    - requests한 html을 받아와서 soup 객체로 넣을 때 parsing 하는 것.
    
        - text화된 html에서 3가지 매서드로 태그를 찾을 수 있다. 
        - find('tag', 속성) : 
        - find_all('tag', 속성) : 
        - select_one : copy css_selector로 가져온 태그로 검색, 가장 첫번째 태그를 추출
        - select : 찾은 모든 selector를 태그 추출하여 리스트로 저장

## Selenium 
> <strong>selenium 라이브러리</strong>은 웹브라우저를 통제하여 파이썬으로 테스트할 때 사용하는 것이 주된 목적이나 크롤링에서도 유용하게 사용할 수 있다. 
> selenium은 하위 패키지에는 <strong>webdriver</strong>가 있다. 
> webdriver의 하위 모듈에는 **Chrome**, **common**, 이 있다. 

 ### webdriver 하위 모듈
> #### 1. Chrome("chromedriver.exe가 설치된 경로") 
    webdriver.Chrome
    
    - **get("웹브라우저 제어할 주소")** : run하면 웹이 실행되면서 페이지가 열린다. 컴퓨터 환경에 따라 열리는 시간은 다르다. 다음 명령 전까지 받아오는 데이터가 있어야 하기 때문에 지연 명령이 있다.
    (아래 support 참고)

    - find_element_by_css_selector() : html css selector 값으로 접근 
    - find_element_by_id() : id 속성으로 접근
    - find_element_by_tag_name : 태그 이름으로 접근
    - find_element_by_xpath() : x-path로 접근
    - find_element_by_class_name : class 속성으로 접근
    - find_element_by_link_text : 링크가 달려 있는 텍스트로 접근
    - find_element_by_partial_link_text : 링크가 달려 있는 엘리먼트에 텍스트 일부만
        **이중**으로 find_element_by를 사용할 수 있다. 
        **find_element_by 하위 매서드** 
        - click() : 접근한 것 클릭
        - send_keys('') : 접근한 것에 ''을 텍스트로 입력하고 enter
        - clear() : 접근한 것의 텍스트 삭제

    - window_handles : 브라우저 탭 객체를 리스트로 반환. 
    - switch_to.window(window_handles[i]) : 지정한 i+1번째 탭으로 이동

    - execute_script('window.scrollTo(0, document.body.scrollHeight)') : 최하단으로 스크롤 이동
    - execute_script('window.scrollTo(0, n)') : n번 스크롤 내리기 

    - 캡처할 엘리먼트.save_screenshot('파일명.jpg) : 스크린샷 캡쳐

    - close() : 제어 중인 웹 브라우저 닫기



> #### 2. support
    - implicitly_wait(int) : int의 시간동안 모든 요소가 로드될 때까지 대기한다. 시간 내에 찾으면 대기는 종료된다. 
    - time 라이브러리를 사용해서 time.sleep(int)를 써도 된다. 
    - implicitly는 명시적인 int를 주기 때문에 효율성이 떨어진다는 단점이 있다. 

    **명시적 조건 대기**
    - expected_conditions : 여러 대기 조건을 가지고 있는 모듈. (as EC)
        - presence_of_element_located('locator특정 요소') : html 내 특정 요소가 존재하게 될 때까지 대기
        - element_attribute_to_include(locator,attribute) : 특정 요소 안에 주어진 attribute가 있을 때까지 대기
        - 이 외에도 많은 매서드가 있다. 참고 (https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions)

    - ui : WebDriverWait이라는 하위 클래스를 가지고 있다. WebDriverWait(Webdriver객체명 , int) 
        - WebDriverWait의 하위 매소드 until('expected_conditions') , int는 최대 대기시간

> #### 3. common
    - (3-1) alert : from selenium.webdriver.common.alert import Alert
        - Alert 
            - Alert(driver).accept() : 팝업창 수락 누름 
            - Alert(driver).dismiss() : 팝업창 거절 누름
            - print(Alert(driver)).text : 경고창 텍스트 얻음
    - (3-2) **by** : element 접근할 때 더 깔끔하게 코딩할 수 있음.  from selenium.webdriver.common.by import By
        - find_element(By.XPATH, 'xpath경로')
        - find_element(By.ID, 'id속성')
        - find_element(By.LINK_TEXT)
        - find_element(By.CLASS_NAME, 'class')
        - find_element(By.CSS_SELECTOR, ' ')
        - find_element(By.TAG_NAME, ' ')





> #### selenium에서 발생할 수 있는 오류
oAlertPresentException 경고창 관련 명령어를 실행했으나 현재 경고창이 뜨지 않음
NoSuchElementException 엘레먼트 접근하였으나 없음
TimeoutException 특정한 액션을 실행하였으나 시간이 오래 지나도록 소식이 없음
ElementNotInteractableException 엘리먼트에 클릭등을 하였으나 클릭할 성질의 엘리먼트가 아님
NoSuchWindowException 해당 윈도우 없음
NoSuchFrameException 해당 프레임 없음
