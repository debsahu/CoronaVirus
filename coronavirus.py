import requests
from bs4 import BeautifulSoup
import datetime
import ifttt_config

x = datetime.datetime.now()
date = x.strftime("%D %T")

base_url = 'https://www.michigan.gov'
corona_main_page = requests.get(base_url + '/coronavirus')

## Parse link to statistics page
soup_link = BeautifulSoup(corona_main_page.text, 'html.parser')
# link = soup_link.find('div', id="block-3_114405").find('span', class_='readLink').find('a', href=True)['href']
link = soup_link.find('a', title='<span class="sr-only">Michigan Data:</span>', href=True)['href']
# print(link)

## Follow the link and parse total michigan statistics
page = requests.get(base_url + link)
soup = BeautifulSoup(page.text, 'html.parser')
pos = soup.find('table').find_all("strong")[-2].text.strip()
death = soup.find('table').find_all("strong")[-1].text.strip()
# print(pos)
print("COVID-19: " + pos + " cases & " + death + " deaths in Michigan as of " + date)

report = {}
report["value1"] = pos
report["value2"] = death
report["value3"] = date
requests.post("https://maker.ifttt.com/trigger/covid19/with/key/" + ifttt_config.api_key, data=report)