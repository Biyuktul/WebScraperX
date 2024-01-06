#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = "https://www.python.org/events/python-events/"
page = urlopen(url)

soup = BeautifulSoup(page.read().decode('utf-8'), 'html')

events = soup.find('ul', {'class': 'list-recent-events'}).find_all('li')

events_list = []
for event in events:
    events_dict = dict()
    events_dict['Name'] = event.find('h3').find('a').get_text()
    events_dict['Location'] = event.find('span', {'class': 'event-location'}).get_text()
    events_dict['Time'] = event.find('time').get_text()
    events_list.append(events_dict)

with open('events.csv', 'w', encoding='utf-8', newline='') as fh:
    field_names = ['Name', 'Location', 'Time']
    writer = csv.DictWriter(fh, fieldnames=field_names)
    
    writer.writeheader()
    for event in events_list:
        writer.writerow(event)

# [print(event) for event in events_list]
