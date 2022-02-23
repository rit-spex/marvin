import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.cleardarksky.com/c/RchstrHYkey.html")

soup = BeautifulSoup(response.text, 'html.parser')

for r in soup.find_all('map'):
    print(r)

#result = lxml_html.xpath("/html")#body/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/noindex/map")