import scrapy

class SpiderCacheItem(scrapy.Item):

	url_md5 = scrapy.Field()

	url = scrapy.Field()

	expire = scrapy.Field()

	content = scrapy.Field()
