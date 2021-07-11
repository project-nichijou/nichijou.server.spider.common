from common.items.common_item import CommonItem
import scrapy


class CommonLogItem(CommonItem):

	table = 'log'

	time = scrapy.Field()

	content = scrapy.Field()
