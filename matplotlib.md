# matplotlib은 데이터 시각화 라이브러리이다. 
> 하위 패키지에는 대표적으로 pyplot, rc, font_manager가 있다.

## pyplot : 시각화 패키지 

    1. style.use('ggplot') : 차트 뒷 배경에 격자 무늬를 넣는다.
    2. figure(figsize=(가로int, 세로int)) : 차트의 전체 사이즈를 설정
    3. title('text') : 차트의 제목 
    4. rcParams['axes.unicode_minus] = False : 시각화하면서 (-) 기호가 깨지는 것을 방지.
    5. rc : rc('font', family = '폰트 영어 이름')
    6. pie(int list, label = [int list와 동일한 갯수의 str로 구성된 리스트], autopct(소수점) = '%.nf%%', colors = color ) : 비율을 자동으로 계산된 파이 차트
    7. plot(x축, y축) : 선 그래프
    8. bar(x축, y축) : 수직 막대 그래프
    9. barh(y축, x축) : 수평 막대 그래프
    10. legend() : 범주
    11. show() : print와 같다. 

    공통적으로 들어가는 속성 : label, color(색 코드 : https://matplotlib.org/gallery/color/named_colors.html)

## rc : 폰트 설정 (from matplotlib import rc)
    rc('font', family = '폰트 영어 이름')

## font_manager (from matplotlib import font_manager)
    .FontProperties(fname=font_path).get_name()

    보통 rc와 font_manager는 같이 쓴다. 
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family = font_name)

