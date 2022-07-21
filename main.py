from BS4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/1968-06-08/"

response = requests.get(URL)
web_page_html = response.text
soup = BeautifulSoup(web_page_html, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story")
print(songs)