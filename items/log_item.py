import scrapy


class CommonLogItem(scrapy.Item):

	time = scrapy.Field()

	content = scrapy.Field()
