from common.items.common_item import CommonItem
import scrapy


class CommonFailedRequestItem(CommonItem):

	table = 'request_failed'

	url_md5 = scrapy.Field()

	url = scrapy.Field()

	spider = scrapy.Field()

	desc = scrapy.Field()
