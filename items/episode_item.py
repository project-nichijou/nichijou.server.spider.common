import scrapy


class CommonEpisodeItem(scrapy.Item):

	id = scrapy.Field()

	type = scrapy.Field()

	sort = scrapy.Field()

	url = scrapy.Field()

	name = scrapy.Field()

	name_cn = scrapy.Field()

	status = scrapy.Field()

	duration = scrapy.Field()

	date = scrapy.Field()

	desc = scrapy.Field()

	sites = scrapy.Field()
