import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

text_lst = []
for i in range(50):
    url = 'https://movie.naver.com/movie/point/af/list.naver?&page='+ str(i)
    html = requests.get(url)
    soup = bs(html.text, 'html.parser')
    body = soup.find('tbody')
    tr_text = body.find_all('tr')

    for tr in tr_text:
        title = tr.find('a', class_='movie color_b').get_text()
        review = tr.find('a', class_='report')['onclick'].split(",")[2]
        score = tr.find('em').get_text()
        date = tr.find_all('td', class_='num')[-1].get_text()[-8:]
        text_lst.append({'title': title, 'review': review, 'score': score, 'date':date})

df = pd.DataFrame(text_lst)

df.to_excel('네이버영화평점.xlsx', encoding='utf8')


