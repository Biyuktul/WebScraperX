#!/usr/bin/python3
"""
scraping python.org website to get recent python events\
    and save the events data to csv
"""
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import csv
import time


def download_webpage(url):
    """
    Download the content from the specified URL.

    Args:
        url (str): The URL of the resource to be downloaded.

    Returns:
        string: The string content of the downloaded resource.


    Example:
        >>> content = download('https://www.example.com')
        >>> print(content)
    """
    try:
        response = urlopen(url).read().decode("utf-8")
    except Exception as e:
        print("Unexpected error occured\nRetrying...")
        for i in range(3):
            try:
                response = urlopen(url).read().decode("utf-8")
            except Exception as e:
                print("Failed")
                time.sleep(5)
        response = None
    return response

url = "https://www.python.org/events/python-events/"
html = download_webpage(url)

if html:
    soup = BeautifulSoup(html, "html")

    events = soup.find("ul", {"class": "list-recent-events"}).find_all("li")

    events_list = []
    for event in events:
        events_dict = dict()
        events_dict["Name"] = event.find("h3").find("a").get_text()
        events_dict["Location"] = event.find(
            "span", {"class": "event-location"}
        ).get_text()
        events_dict["Time"] = event.find("time").get_text()
        events_list.append(events_dict)

    with open("events.csv", "w", encoding="utf-8", newline="") as fh:
        field_names = ["Name", "Location", "Time"]
        writer = csv.DictWriter(fh, fieldnames=field_names)

        writer.writeheader()
        for event in events_list:
            writer.writerow(event)
