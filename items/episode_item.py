from common.items.common_item import CommonItem
import scrapy


class CommonEpisodeItem(CommonItem):

	table = 'episode'

	primary_keys = ['id', 'sort', 'type']

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
