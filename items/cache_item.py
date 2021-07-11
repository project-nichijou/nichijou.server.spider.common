from common.items.common_item import CommonItem
import scrapy


class CommonCacheItem(CommonItem):

	table = 'cache'

	url_md5 = scrapy.Field()

	url = scrapy.Field()

	expire = scrapy.Field()

	content = scrapy.Field()
