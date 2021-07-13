from common.items.common_item import CommonItem
import scrapy


class CommonLogItem(CommonItem):

	table = 'log'

	primary_keys = []

	use_fail = False

	time = scrapy.Field()

	content = scrapy.Field()
