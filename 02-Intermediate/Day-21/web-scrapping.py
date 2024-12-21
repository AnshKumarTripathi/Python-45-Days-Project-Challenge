import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = []
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        headings.append({'tag': heading.name, 'text': heading.text.strip()})
    return headings

url = 'https://www.pygame.org/docs/'

html_content = get_html_content(url)
if html_content:
    print('Fetched HTML Content:')
    print(html_content[:1000])  
    headings = parse_html(html_content)
    print('Extracted Headings:')
    with open('extracted_headings.txt', 'w', encoding='utf-8') as file:
        for heading in headings:
            print(f"Tag: {heading['tag']}\nText: {heading['text']}\n")
            file.write(f"Tag: {heading['tag']}\nText: {heading['text']}\n\n")
else:
    print('Failed to retrieve the web page content')
