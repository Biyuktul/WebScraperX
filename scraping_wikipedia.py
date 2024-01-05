from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = urlopen(url)

soup = BeautifulSoup(page.read().decode('utf-8'), 'html.parser')

table = soup.find_all('table')[1]
rows = table.find_all('tr')

for row in rows:
    data = row.find_all('td')
    indiv = [i.get_text().strip() for i in data]
    print(indiv)