import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
	try:
		r = requests.get(url, timeout = 30)
		#抛异常
		r.raise_for_status()
		#s设置编码
		r.encoding = r.apparent_encoding
		#print(r.text)
		return r.text
	except:
		return "Failed"

def fillUnivList(ulist, html):
	soup = BeautifulSoup(html, "lxml")
	for tr in soup.find("tbody").children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr("td")
			ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
	tplt = "{:<10}{:<10}{:<10}"
	print(tplt.format("排名", "学习名称", "总分"))
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0], u[1], u[2]))

def main():
	uinfo = []
	url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
	html = getHtmlText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 10)

main()