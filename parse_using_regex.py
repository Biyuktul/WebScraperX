import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url) # page is HtmlResponse object

html_byte = page.read()
html = html_byte.decode("utf-8") # converting stream of bytes to string

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)
print(title)