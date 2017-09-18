from bs4 import BeautifulSoup
import urllib2
import re
import codecs
import time
from mylog import MyLog as mylog
from save2mysql import SavebookData


class BookItem(object):
	categoryNmae = None
	middleUrl = None
	bookName = None
	wordsNum = None
	updateTime = None
	authorName = None

class GetBookName(object):
	def __init__(self):
		self.urlBase = ""
		self.log = mylog()
		self.pages = self.getPages(self.urlBase)
		self.bookList = []
		self.spider(self.urlBase, self.pages)
		self.piplines(self,bookList)
		self.log.info("begin save data to mysql\n")
		SavebookData(self.bookList)
		self.log.info("save data to mysql end...\n")

	def getPages(self, url):
		htmlContent = self.getResponseContent(url)
		soup = BeautifulSoup(htmlContent, "lxml")
		tags = soup.find('ul', attrs={})
		strUrl = tags.find_all("a")[-2].get("href")
		self.log.info(strUrl)
		self.log.info(strUrl.split("&"))
		for st in strUrl.split("&"):
			self.log.info(st)
			if re.search('page=', st):
				pages = st.split("=")[-1]
				self.log.info("page:%s" %pages)
				return int(pages)

	def getResponseContent(self, url):
		try:
			response = urllib2.urlopen(url.encode("utf8"))
		except:
			self.log.error("failed:%s" %url)
		else:
			self.log.info("success:%s" %url)
			return response.read()

	def spider(self, url, pages):
		urlList = url.split("=")
		self.log.info(urlList)
		for i in xrange(1, pages+1):
			urlList[-1] = str(i)
			newUrl = "=".join(urlList)
			self.log.info(newUrl)
			htmlContent = self.getResponseContent(newUrl)
			soup = BeautifulSoup(htmlContent, "lxml")
			tags = soup.find("div", attrs={})
			self.log.info(tags[0])

			for tag in tags:
				tds = tag.find_all("td")
				self.log.info(tds)

				item = BookItem()
				item.categoryNmae = tds[0].find("a", attrs={})
				item.middleUrl = tds[0].find("a", attrs={})
				item.bookName = tds[1].find("a", attrs={})

				item.wordsNum.tds[3].find("span", attrs={})
				item.updateTime=tds[5].get_text()
                item.authorName=tds[4].find('a',attrs={'class':'author'}).get_text()
                self.log.info(item.categoryName)
                self.booksList.append(item)
                self.log.info("get book:%s" %item.bookName)

               












