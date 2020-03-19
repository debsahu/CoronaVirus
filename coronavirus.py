import requests
from bs4 import BeautifulSoup
import datetime

x = datetime.datetime.now()
date = x.strftime("%D %T")

base_url = 'https://www.michigan.gov'
corona_main_page = requests.get(base_url + '/coronavirus')

## Parse link to statistics page
soup_link = BeautifulSoup(corona_main_page.text, 'html.parser')
link = soup_link.find_all('span', {'class': 'readLink'})[0].find('a', href=True)['href']
# print(link)

## Follow the link and parse total michigan statistics
page = requests.get(base_url + link)
soup = BeautifulSoup(page.text, 'html.parser')
pos = soup.find('table').find_all("strong")[-1].text.strip()
# print(pos)
print(pos + " confirmed COVID-19 cases in Michigan as of " + date)

report = {}
report["value1"] = pos
report["value2"] = date
requests.post("https://maker.ifttt.com/trigger/covid19/with/key/XXXXXXXXXXXXXXXXXXXX", data=report)