# Mensa の申込状況の確認
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

page = requests.get("https://mensa.jp/exam/")
bs = BeautifulSoup(page.content, 'html.parser')

#images = bs.find_all('img', {'src':re.compile('skin/default/image/exam/entry_(out|quota).jpg')})
images = bs.find_all('img', {'alt':re.compile('(満員|締切|申し込む)')})
for image in images:
    print(image['alt'])
    
