# app.py

from flask import Flask, render_template, request, jsonify
from datetime import datetime
from jinja2 import Undefined
app = Flask(__name__)

def convert_to_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

# 더미 뉴스 데이터
dummy_news_data = [
    {"title": "Rafah crossing: More than 100 Britons leave Gaza but dozens remain", "url": "https://www.bbc.com/news/uk-67325584?at_medium=RSS&at_campaign=KARANGA", "date": "2023-11-01"},
    {"title": "Suella Braverman: Home secretary criticised for NI 'hate marches' remark", "url": "https://www.bbc.com/news/uk-northern-ireland-67366165", "date": "2023-11-02"},
    {"title": "Michelle O'Neill awarded no damages over kennel remark", "url": "https://www.bbc.com/news/northern_ireland/northern_ireland_politics", "date": "2023-11-01"},
    {"title": "4 세 미만의 어머니 10 명 중 1 명은 육아를 통해 일을 그만두 었다고 자선 단체는 말합니다.","url":"https://www.bbc.co.uk/news/business-67325993?at_medium=RSS&at_campaign=KARANGA","date":"2023-11-20"},
    {"title": "시청 : '치명적인'Bognor Regis 홍수 현장에서","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-09-03"}
    # 실제 데이터는 더 많을 것입니다.
]

@app.route('/')
def index():
    # 날짜별로 뉴스 데이터 정리
    sorted_news_data = sorted(dummy_news_data, key=lambda x: convert_to_datetime(x['date']), reverse=True)
    cleaned_news_data = [{k: v if v is not None else None for k, v in news.items()} for news in sorted_news_data]
    return  render_template('index.html', news_data=sorted_news_data or [])

@app.route('/search_news', methods=['POST'])
def search_news():
    search_term = request.form['searchTerm']

    # 검색어에 맞는 뉴스 데이터를 가져오는 부분
    searched_news_data = [news for news in dummy_news_data if search_term.lower() in news['title'].lower()]
    sorted_news_data = sorted(searched_news_data, key=lambda x: convert_to_datetime(x['date']), reverse=True)

    return jsonify({'newsData': sorted_news_data})

@app.route('/article/<title>')
def article(title):
    # 기사의 title을 이용하여 기사의 URL을 가져오는 로직
    for news in dummy_news_data:
        if news['title'] == title:
            return f'이 기사의 URL: {news["url"]}'
    
    return '기사를 찾을 수 없습니다.'

if __name__ == '__main__':
    app.run(debug=True)
