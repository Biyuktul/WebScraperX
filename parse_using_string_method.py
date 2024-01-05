from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url) # page is HtmlResponse object

html_byte = page.read()
html = html_byte.decode("utf-8") # converting stream of bytes to string

start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]
print(title)