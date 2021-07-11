import scrapy


class CommonAnimeNameItem(scrapy.Item):

	id = scrapy.Field()

	name = scrapy.Field()
