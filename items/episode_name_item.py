import scrapy


class CommonEpisodeNameItem(scrapy.Item):

	id = scrapy.Field()

	type = scrapy.Field()

	sort = scrapy.Field()

	name = scrapy.Field()
