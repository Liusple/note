from bs4 import BeautifulSoup
import urllib.request
import re
import codecs
import time
from mylog import MyLog as mylog
#from save2mysql import SavebookData


class BookItem(object):
	categoryNmae = None
	middleUrl = None
	bookName = None
	wordsNum = None
	updateTime = None
	authorName = None

class GetBookName(object):
	def __init__(self):
		self.urlBase = "http://a.qidian.com/?action=1&orderId=&style=2&page=1"
		self.log = mylog()
		self.pages = self.getPages(self.urlBase)
		self.booksList = []
		self.spider(self.urlBase, self.pages)
		self.piplines(self.booksList)
		#self.log.info("begin save data to mysql\n")
		#SavebookData(self.booksList)
		#self.log.info("save data to mysql end...\n")

	#得到页数
	def getPages(self, url):
		htmlContent = self.getResponseContent(url)
		soup = BeautifulSoup(htmlContent, "lxml")
		tags = soup.find('ul', attrs={"class":"lbf-pagination-item-list"})
		strUrl = tags.find_all("a")[-2].get("href")
		self.log.info(strUrl)
		self.log.info(strUrl.split("&"))
		for st in strUrl.split("&"):
			if re.search('page=', st):
				pages = st.split("=")[-1]
				self.log.info("page:%s" %pages)
				return int(pages)

	def getResponseContent(self, url):
		try:
			response = urllib.request.urlopen(url)
		except:
			self.log.error("failed:%s" %url)
		else:
			self.log.info("success:%s" %url)
			#print(response.read().decode("utf-8"))
			return response.read()

	def spider(self, url, pages):
		urlList = url.split("=")
		self.log.info(urlList)
		for i in range(1, pages+1):
			#拼接为新的url
			urlList[-1] = str(i)
			newUrl = "=".join(urlList)
			#self.log.info(newUrl)
			htmlContent = self.getResponseContent(newUrl)
			soup = BeautifulSoup(htmlContent, "lxml")
			tags = soup.find("div", attrs={"class":"main-content-wrap fl"}).find("div", attrs={"class":"all-book-list"}).find("tbody").find_all("tr")
			#self.log.info(tags[0])

			for tag in tags:
				tds = tag.find_all("td")
				#self.log.info(tds)
				#self.log.info("\n")
				item = BookItem()
				item.categoryName = tds[0].find("a", attrs={"class":"type"}).get_text() + tds[0].find("a", attrs={"class": 'go-sub-type'}).get_text()
				item.middleUrl = tds[0].find("a", attrs={"class":"type"}).get("href")
				item.bookName = tds[1].find("a", attrs={"class":"name"}).get_text()

				item.wordsNum = tds[3].find("span", attrs={"class":"total"}).get_text()
				item.updateTime = tds[5].get_text()
				item.authorName = tds[4].find('a',attrs={'class':'author'}).get_text()
				self.booksList.append(item)
				#self.log.info("book info:%s %s %s %s" %(item.categoryName, item.bookName, item.wordsNum, item.authorName))

	def piplines(self, bookList):
		bookName = "qidian.txt"
		nowTime = time.strftime('%Y-%m-%d %H:%M:%S \r\n',time.localtime())
		with codecs.open(bookName, "w", "utf8") as fp:
			fp.write("run time:%s" %nowTime)
			for item in self.booksList:
				fp.write("%s\t %s\t\t %s\t\t %s\t\t %s\r\n" %(item.categoryName, item.bookName, item.wordsNum, item.updateTime, item.authorName))
   
if __name__ == "__main__":
	GBN = GetBookName()












