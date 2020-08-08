from django.test import TestCase

# Create your tests here.
#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
from requests_html import HTMLSession
session = HTMLSession()
import sqlite3


headers = {
    'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

response = session.get(
        'https://y.qq.com/n/yqq/toplist/27.html#stat=y_new.toplist.menu.27',headers=headers)
soup = bs(response.content, 'html.parser')
boxes = soup.find_all('ul', class_='songlist__list')
for box in boxes:
    print(box.find('div', class_='songlist__number').text)
    print(box.find('div',class_='songlist__songname').span.a.text)
    print(box.find('div', class_='songlist__artist').a.text)
    print(box.find('div', class_='songlist__time').text)
        #my_set.insert_one({'id': id, 'song_name': song_name,'singer_name':singer_name,'times':times})

