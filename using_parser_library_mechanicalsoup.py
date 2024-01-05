import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)

login_html = page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

result_page = browser.submit(form, page.url)
links = result_page.soup.select("a")