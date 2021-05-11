from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st


url = "https://www.fvt.co.jp/news.html"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

contents = soup.find('div', {'class': 'contents'})

news_lists = []
news_dates = contents.find_all('div', {'class': 'news_date'})
new_kijis = contents.find_all('div', {'class': 'news_kiji01'})

kiji_list = []

for new_kiji in new_kijis:
    if len(new_kiji) > 0:
        new_kiji = new_kiji.text.replace('\n\xa0\xa0\n', '').replace(
            '\n', '').replace('\xa0\xa0', '').strip(' ')
        kiji_list.append(new_kiji)

for news_date, news_kiji in zip(news_dates, kiji_list):
    news_list = {}
    news_list['日付'] = news_date.text.replace('\n\xa0\xa0\n', '').replace(
        '\n', '').replace('\xa0\xa0', '').strip(' ')
    news_list['記事'] = news_kiji
    news_lists.append(news_list)

df = pd.DataFrame(news_lists)

st.title('FVTのニュース')
st.write('### 最新のニュース一欄', df)
