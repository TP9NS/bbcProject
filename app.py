# app.py

from flask import Flask, render_template, request, jsonify
from datetime import datetime
from jinja2 import Undefined
import random as rand
from operator import itemgetter
from datetime import timedelta
app = Flask(__name__)

def convert_to_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')
#키워드
keywords = [" ","어머니", "test", "Rafah", "O"]
# 더미 뉴스 데이터
dummy_news_data = [
    {"title": "Rafah crossing: More than 100 Britons leave Gaza but dozens remain", "url": "https://www.bbc.com/news/uk-67325584?at_medium=RSS&at_campaign=KARANGA", "date": "2023-11-01","subcategory":"test"},
    {"title": "Suella Braverman: Home secretary criticised for NI 'hate marches' remark", "url": "https://www.bbc.com/news/uk-northern-ireland-67366165", "date": "2023-11-02","subcategory":"test"},
    {"title": "Michelle O'Neill awarded no damages over kennel remark", "url": "https://www.bbc.com/news/northern_ireland/northern_ireland_politics", "date": "2023-11-01","subcategory":"test"},
    {"title": "4 세 미만의 어머니 10 명 중 1 명은 육아를 통해 일을 그만두 었다고 자선 단체는 말합니다.","url":"https://www.bbc.co.uk/news/business-67325993?at_medium=RSS&at_campaign=KARANGA","date":"2023-11-20","subcategory":"test"},
    {"title": "시청 : '치명적인'Bognor Regis 홍수 현장에서","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-09-03","subcategory":"test"},
    {"title": "DJ는 필리핀에서 라이브 방송 중에 죽음을 맞았습니다","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-10-08","subcategory":"어머니"},
    {"title": "소매 업체의 붕괴 후 Wilko 노동자","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-10-11","subcategory":"test"},
    {"title": "resc-beewed : 해안선에서 구한 영국의 외로운 양","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-03-03","subcategory":"어머니"},
    {"title": "Matthew Perry는 개인 행사에 묻힌 미국 언론 보도","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-10-03","subcategory":"test"},
    {"title": "Bowen : 4 주간의 이스라엘-가자 전쟁 후 5 개의 새로운 현실","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"어머니"},
    {"title": "이스라엘은 하마스가 터널에서 히트 앤 런 공격을했다","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"RAFAH"},
    {"title": "레바논의 헤즈볼라는 무엇이며 이스라엘과 전쟁을 할 것인가?","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"test"},
    {"title": "그들이 어머니에게 전화했을 때, Hamas는 전화에 응답했습니다.","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"test"},
    {"title": "Rafah crossing: More than 100 Britons leave Gaza but dozens remain", "url": "https://www.bbc.com/news/uk-67325584?at_medium=RSS&at_campaign=KARANGA", "date": "2023-11-01","subcategory":"test"},
    {"title": "Suella Braverman: Home secretary criticised for NI 'hate marches' remark", "url": "https://www.bbc.com/news/uk-northern-ireland-67366165", "date": "2023-11-02","subcategory":"test"},
    {"title": "Michelle O'Neill awarded no damages over kennel remark", "url": "https://www.bbc.com/news/northern_ireland/northern_ireland_politics", "date": "2023-11-01","subcategory":"test"},
    {"title": "4 세 미만의 어머니 10 명 중 1 명은 육아를 통해 일을 그만두 었다고 자선 단체는 말합니다.","url":"https://www.bbc.co.uk/news/business-67325993?at_medium=RSS&at_campaign=KARANGA","date":"2023-11-20","subcategory":"test"},
    {"title": "시청 : '치명적인'Bognor Regis 홍수 현장에서","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-09-03","subcategory":"test"},
    {"title": "DJ는 필리핀에서 라이브 방송 중에 죽음을 맞았습니다","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-10-08","subcategory":"어머니"},
    {"title": "소매 업체의 붕괴 후 Wilko 노동자","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-10-11","subcategory":"test"},
    {"title": "resc-beewed : 해안선에서 구한 영국의 외로운 양","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-03-03","subcategory":"어머니"},
    {"title": "Matthew Perry는 개인 행사에 묻힌 미국 언론 보도","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-10-03","subcategory":"test"},
    {"title": "Bowen : 4 주간의 이스라엘-가자 전쟁 후 5 개의 새로운 현실","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"어머니"},
    {"title": "이스라엘은 하마스가 터널에서 히트 앤 런 공격을했다","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"RAFAH"},
    {"title": "레바논의 헤즈볼라는 무엇이며 이스라엘과 전쟁을 할 것인가?","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"test"},
    {"title": "그들이 어머니에게 전화했을 때, Hamas는 전화에 응답했습니다.","url":"https://www.bbc.co.uk/news/uk-67324354?at_medium=RSS&at_campaign=KARANGA","date":"2023-12-03","subcategory":"test"}
    # 실제 데이터는 더 많을 것입니다.
]
sorted_news_data = sorted(dummy_news_data, key=lambda x: convert_to_datetime(x['date']), reverse=True)

categories = {
    "스포츠": ["어머니", "test", "Rafah", "O"],
    "기술": ["자동차", "IT", "핸드폰"],
    "취미":["영화","여행","요리"]
}
@app.route('/')
def index():
    # 날짜별로 뉴스 데이터 정리``
    random_news_data = rand.sample(dummy_news_data, 24)
    sorted_random_news_data = sorted(random_news_data, key=itemgetter("date"), reverse=True)
    cleaned_news_data = [{k: v if v is not None else None for k, v in news.items()} for news in sorted_news_data]
   
    return  render_template('index.html', news_data=sorted_random_news_data or [],keywords=keywords,categories=categories)

@app.route('/search_by_keyword', methods=['POST'])
def search_by_keyword():
    keyword = request.form.get('keyword')
    
    # 키워드에 해당하는 뉴스 데이터 필터링
    filtered_news = [news_item for news_item in dummy_news_data if keyword.lower() in news_item['title'].lower()]

    return jsonify({'newsData': filtered_news})


@app.route('/search_news', methods=['POST'])
def search_news():
    search_term = request.form['searchTerm']
    selected_period = request.form['period']

    # 검색어와 선택된 기간에 맞는 뉴스 데이터 가져오기
    searched_news_data = [news for news in dummy_news_data if search_term.lower() in news['title'].lower() and filter_by_period(news['date'], selected_period)]
    sorted_news_data = sorted(searched_news_data, key=lambda x: convert_to_datetime(x['date']), reverse=True)

    return jsonify({'newsData': sorted_news_data})

# 추가된 함수: 날짜를 기반으로 기간 필터링
def filter_by_period(news_date, selected_period):
    if selected_period == 'all':
        return True
    else:
        news_datetime = convert_to_datetime(news_date)
        today = datetime.today()
        if selected_period == '1day':
            return (today - timedelta(days=1)) <= news_datetime <= today
        elif selected_period == '1week':
            return (today - timedelta(weeks=1)) <= news_datetime <= today
        elif selected_period == '1month':
            return (today - timedelta(days=30)) <= news_datetime <= today
        else:
            return False
@app.route('/search_by_category', methods=['POST'])
def search_by_category():
    category = request.form.get('category')
    subcategory = request.form.get('subcategory')

    # 카테고리에 해당하는 뉴스 데이터 필터링
    
    filtered_news = [news_item for news_item in dummy_news_data if subcategory.lower() == news_item.get('subcategory').lower()]

    return jsonify({'newsData': filtered_news})
@app.route('/article/<title>')
def article(title):
    # 기사의 title을 이용하여 기사의 URL을 가져오는 로직
    for news in dummy_news_data:
        if news['title'] == title:
            return f'이 기사의 URL: {news["url"]}'
    
    return '기사를 찾을 수 없습니다.'

if __name__ == '__main__':
    app.run(debug=True)
