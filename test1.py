import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os, re, csv
import usecsv
import urllib.request as ur
from googletrans import Translator

rss_url = 'https://feeds.bbci.co.uk/news/rss.xml'

response = requests.get(rss_url)

soup = bs(response.content, 'xml')

data = []

translator = Translator()

items = soup.find_all('item')

for idx, item in enumerate(items, start=1):
    title = item.title.text
    tranlation_title = translator.translate(title, dest = 'ko')
    link = item.link.text
    pub_date = item.pubDate.text
    pub_date_formatted = pd.to_datetime(pub_date).strftime('%Y-%m-%d')
    data.append([idx, pub_date_formatted, tranlation_title.text, link])

df = pd.DataFrame(data, columns=['번호', '날짜', '기사 제목', 'URL'])

df.to_excel(r'news_data.xlsx', index=False, engine='openpyxl')

df = pd.read_excel(r'news_data.xlsx', engine='openpyxl')
print(df) 