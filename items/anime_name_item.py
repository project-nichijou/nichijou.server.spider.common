from common.items.common_item import CommonItem
import scrapy


class CommonAnimeNameItem(CommonItem):

	table = 'anime_name'

	primary_keys = ['id', 'name']

	id = scrapy.Field()

	name = scrapy.Field()
