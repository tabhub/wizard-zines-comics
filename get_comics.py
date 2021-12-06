from bs4 import BeautifulSoup
import requests

resp = requests.get("https://wizardzines.com/comics/")
soup = BeautifulSoup(resp.content, "html.parser")
for link in soup.findAll('a'):
    href = link.get('href')
    if href.startswith("/comics/"):
        name = href.split("/")[2]
        image_url = "https://wizardzines.com/comics/{0}/{0}.png".format(name)
        r = requests.get(image_url)
        open("./images/{}.png".format(name), 'wb').write(r.content)
