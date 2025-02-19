from bs4 import BeautifulSoup
import os
import requests

def get_html(filepath, url):
    if os.path.exists(filepath):
        print('File exists, loading cached html...')
        with open(filepath, 'r') as file:
            html = file.read()
    else:
        print('No file found, loading html from site...')
        response = requests.get(url)
        html = response.text
        with open(filepath, 'w') as file:
            file.write(html)

    return html

html = get_html('hacker_news.html', 'https://news.ycombinator.com/')
soup = BeautifulSoup(html, 'html.parser')

tags = soup.select('[href^="http"]:not([href*="ycombinator.com"])') # <span class="titleline clickable-link">
outgoing_urls = [tag.get('href') for tag in tags]

for i, url in enumerate(outgoing_urls):
    get_html(f'scrape-html-{i}.html', url)