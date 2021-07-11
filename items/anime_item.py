import scrapy


class CommonAnimeItem(scrapy.item):

	id = scrapy.Field()

	url = scrapy.Field()

	name = scrapy.Field()

	name_cn = scrapy.Field()

	desc = scrapy.Field()

	eps_cnt = scrapy.Field()

	date = scrapy.Field()

	weekday = scrapy.Field()

	meta = scrapy.Field()

	tags = scrapy.Field()

	type = scrapy.Field()

	image = scrapy.Field()

	rating = scrapy.Field()

	rank = scrapy.Field()

	related = scrapy.Field()

	sites = scrapy.Field()
