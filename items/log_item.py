import scrapy


class SpiderLogItem(scrapy.Item):

	time = scrapy.Field()

	content = scrapy.Field()
