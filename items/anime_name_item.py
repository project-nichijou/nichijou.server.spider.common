import scrapy


class SpiderAnimeNameItem(scrapy.Item):

	id = scrapy.Field()

	name = scrapy.Field()
