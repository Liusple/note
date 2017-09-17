import requests
import requests_cache
from bs4 import BeautifulSoup
import os
import time

requests_cache.install_cache("demo_cache")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}

reponse = requests.get("http://www.dy2018.com/html/gndy/dyzz/index.html", headers=headers)
html_doc = reponse.content.decode("gbk")
#print(html_doc)

soup = BeautifulSoup(html_doc, "lxml")
links = []
for l in soup.select(".ulink"):
	href = "http://www.dy2018.com" + l["href"]
	title = l.string
	links.append(href)
	#print(href, title)
	
for link in links:
	reponse = requests.get(link, headers=headers)
	html_doc = reponse.content.decode("gbk")
	soup = BeautifulSoup(html_doc, "lxml")
	ftp_elememt = soup.select("#Zoom table a")[0]
	down_link = ftp_elememt["href"]
	print(down_link)
	time.sleep(1)