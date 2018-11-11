'''
파일 설명 :
일정시간마다 웹페이지를 크롤링하여, 그 값이 변하면 출력하도록 함

시나리오 1 ) requests  를 통해 웹페이지의 정보를 받아온다.
시나리오 2 ) BeautifulSoup라는 Wrapper를 통해 어떤 css에 해당하는 값만 빼온다
시나리오 3 ) 기존에 빼온 값과 새로 빼온 값을 비교한다

https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
'''

import requests

## HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

## HTML 소스 가져오기
html = req.text
## HTTP Header 가져오기
header = req.headers
## HTTP Status 가져오기 (200: 정상)
status = req.status_code
## HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok
