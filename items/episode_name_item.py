from common.items.common_item import CommonItem
import scrapy


class CommonEpisodeNameItem(CommonItem):

	table = 'episode_name'

	id = scrapy.Field()

	type = scrapy.Field()

	sort = scrapy.Field()

	name = scrapy.Field()
