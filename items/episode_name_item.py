import scrapy


class SpiderEpisodeNameItem(scrapy.Item):

	id = scrapy.Field()

	type = scrapy.Field()

	sort = scrapy.Field()

	name = scrapy.Field()
