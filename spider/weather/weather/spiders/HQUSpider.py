# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class HquspiderSpider(scrapy.Spider):
	name = 'HQUSpider'
	allowed_domains = ['tianqi.com']
	citys = ["quanzhou"]
	start_urls = []
	for city in citys:
		start_urls.append("http://" + city + ".tianqi.com/")
		print("================================")
		print(start_urls)

	def parse(self, response):
		subSelector = response.xpath("//div[@class='tqshow1']")
		print("================================")
		print("subSelector:", subSelector)
		items = []
		for sub in subSelector:
			item = WeatherItem()
			cityDates = ""
			for cityDate in sub.xpath("./h3//text()").extract():
				print("city:Date", cityDate)
				cityDates += cityDate
			item["cityDate"] = cityDates
			item["week"] = sub.xpath("./p//text()").extract()[0]
			item["img"] = sub.xpath("./ul/li[1]/img/@src").extract()[0]
			temps = ""
			for temp in sub.xpath("./ul/li[2]//text()").extract():
				temps += temp
			item['temperature'] = temps
			item['weather'] = sub.xpath('./ul/li[3]//text()').extract()[0]
			item['wind'] = sub.xpath('./ul/li[4]//text()').extract()[0]
			items.append(item)
			print(items)
		return items

