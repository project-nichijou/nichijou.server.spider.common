from common.items.common_item import CommonItem
import scrapy


class CommonAnimeItem(CommonItem):

	table = 'anime'

	primary_keys = ['id']

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
