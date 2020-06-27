import urllib.request as req
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = req.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
results = soup.select('span.value')
#print("원달러 환율: ",results[0].string) #원달러 환율
#print('원엔 환율: ',results[1].string) #원엔 환율
#print('원유로 황율:', results[2].string) #원유로 환율

url2 = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105'
response2 = req.urlopen(url2)
soup2 = BeautifulSoup(response2, 'html.parser')
results2 = soup2 .select('#section_body a')
for result2 in results2:
	print(result2.attrs['href'])