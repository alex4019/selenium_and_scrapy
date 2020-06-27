from bs4 import BeautifulSoup

html = """
<html><body>
<div id = 'wikibooks'>
	<h1>위키북스 도서</h1>
	<ul class = 'items'>
		<li>유니티 게임 이펙트 입문</li>
		<li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
		<li>모던 웹사이트 디자인의 정석</li>
	</ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
header = soup.select_one('div#wikibooks > h1')
list_items = soup.select('ul.items > li')

print(header.string)
print(soup.select_one('ul').attrs)


for li in list_items:
	print('li = ', li.string)