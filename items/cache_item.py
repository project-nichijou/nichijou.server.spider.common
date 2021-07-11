import scrapy

class CommonCacheItem(scrapy.Item):

	url_md5 = scrapy.Field()

	url = scrapy.Field()

	expire = scrapy.Field()

	content = scrapy.Field()
