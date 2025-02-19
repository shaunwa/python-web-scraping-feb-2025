import os
import requests
from lxml import html

def get_html(filepath, url):
    if os.path.exists(filepath):
        print('File exists, loading cached html...')
        with open(filepath, 'r') as file:
            html_string = file.read()
    else:
        print('No file found, loading html from site...')
        response = requests.get(url)
        html_string = response.text
        with open(filepath, 'w') as file:
            file.write(html_string)

    return html_string

html_string = get_html('hacker_news.html', 'https://news.ycombinator.com/')

tree = html.fromstring(html_string)
tags = tree.xpath('//a/@href')

for tag in tags:
    print(tag)