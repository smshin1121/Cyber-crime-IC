import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('C:/Users/forenshin/Desktop/Cyber-crime-IC/.verification/scattered_spider_doj.html','r',encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
# DOJ pages typically: title, date, body
title = soup.find('h1')
print('TITLE:', title.get_text(strip=True) if title else 'NONE')

# date
date = soup.select_one('time') or soup.select_one('.field--name-field-pr-date')
print('DATE TAG:', date.get_text(strip=True) if date else 'NONE')

# main content
body = soup.select_one('article') or soup.select_one('main') or soup.select_one('.field--name-field-pr-body')
if not body:
    body = soup.body
text = body.get_text('\n', strip=True)
print('---BODY---')
print(text[:8000])
print('---END---')
print('total length:', len(text))
