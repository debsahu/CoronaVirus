import requests
from bs4 import BeautifulSoup
import datetime

x = datetime.datetime.now()
date = x.strftime("%D")
page = requests.get('https://www.michigan.gov/coronavirus')

soup = BeautifulSoup(page.text, 'html.parser')
pos = soup.find_all('span', {'class': 'shortdesc'})[1].find_all('strong')[4].text.strip()

print(pos + " confirmed COVID-19 cases in Michigan as of " + date)

report = {}
report["value1"] = pos
report["value2"] = date
requests.post("https://maker.ifttt.com/trigger/covid19/with/key/XXXXXXXXXXXXXXXXXXXX", data=report)