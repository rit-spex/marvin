from calendar import month
from sched import scheduler
import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.cleardarksky.com/c/RchstrHYkey.html")

soup = BeautifulSoup(response.text, 'html.parser')

result = soup.find_all('area')

# print(result)

schedule = {}

for r in result:
    temp_str = str(r.get('title')) + str(r.get('coords'))
    temp = temp_str.split(' ', 1)
    schedule[temp[0]] = temp_str






#result = lxml_html.xpath("/html")#body/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/noindex/map")