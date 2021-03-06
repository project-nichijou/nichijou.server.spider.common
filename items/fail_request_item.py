from common.items.common_item import CommonItem
import scrapy


class CommonFailedRequestItem(CommonItem):

	table = 'request_failed'

	primary_keys = ['url_md5', 'spider']

	use_fail = False

	url_md5 = scrapy.Field()

	url = scrapy.Field()

	spider = scrapy.Field()

	desc = scrapy.Field()

	params = scrapy.Field()
