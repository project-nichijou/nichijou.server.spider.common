from common.items.common_item import CommonItem
import scrapy


class CommonLogItem(CommonItem):

	table = 'log'

	primary_keys = []

	time = scrapy.Field()

	content = scrapy.Field()
