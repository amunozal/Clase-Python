import scrapy
from prueba.items import PruebaItem

class CoderSpider(scrapy.Spider):
	name = 'coder'
	alowed_domains = ['coder.mx']
	star_urls = ['http://coder.mx/menu.html']

	def parse(self, response):
		item = PruebaItem()
		item['platillo'] = response.xpath('//dt').extract()
		item['precio'] = response.css('.precio').extract()
		return item
