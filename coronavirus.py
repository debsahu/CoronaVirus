import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.michigan.gov/coronavirus')

soup = BeautifulSoup(page.text, 'html.parser')
th = soup.find_all('span', {'class': 'shortdesc'})[1].find_all('td')

date = th[1].text.strip()
all_tested = th[3].text.strip()
neg = th[5].text.strip()
pos = th[7].text.strip()
pending = th[9].text.strip()

print(pos + " confirmed COVID-19 cases in Michigan on " + date)