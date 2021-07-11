import scrapy


class SpiderFailedRequestItem(scrapy.Item):

	url_md5 = scrapy.Field()

	url = scrapy.Field()

	spider = scrapy.Field()

	desc = scrapy.Field()
