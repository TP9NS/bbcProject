import requests
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Session 생성
s = requests.Session()
# 헤더 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

req = s.get('http://feeds.bbci.co.uk/news/rss.xml', headers=headers)

## HTML 소스 가져오기
html = req.text

bs = BeautifulSoup(html, "html.parser")  # BeautifulSoup 객체 생성
data = []
cnt = 0
for item in bs.find_all('item'):  # item과 그 내의 자식요소만 필터링
    data.append([])
    data[cnt].append(item.find('title').get_text())  # title 요소의 텍스트 추출
    data[cnt].append(item.find('description').get_text())  # description 요소의 텍스트 추출
    
    # Find the link element and extract the URL
    link_element = item.find('link')
    if link_element is not None and link_element.text.strip():
        data[cnt].append(link_element.text.strip())
    else:
        # If no link element is found, you can check the 'guid' element as an alternative source for the link.
        guid_element = item.find('guid')
        if guid_element is not None and guid_element.text.strip():
            data[cnt].append(guid_element.text.strip())
        else:
            data[cnt].append('No link available')

    cnt += 1
print(html)
print(data[:1])
