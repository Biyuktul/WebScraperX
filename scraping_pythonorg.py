#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events/"
page = urlopen(url)

soup = BeautifulSoup(page.read().decode('utf-8'), 'html')

events = soup.find('ul', {'class': 'list-recent-events'}).find_all('li')

events_list = []
for event in events:
    events_dict = dict()
    events_dict['name'] = event.find('h3').find('a').get_text()
    events_dict['location'] = event.find('span', {'class': 'event-location'}).get_text()
    events_dict['time'] = event.find('time').get_text()
    events_list.append(events_dict)

[print(event) for event in events_list]
