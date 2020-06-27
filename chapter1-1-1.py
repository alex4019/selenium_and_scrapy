import urllib.request

url = "http://api.aoikujira.com/ip/ini"
savename = 'test2.png'

mem = urllib.request.urlopen(url).read()
print(mem.decode('utf-8'))

url2 = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF'
