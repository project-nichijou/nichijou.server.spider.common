import scrapy


class CommonItem(scrapy.Item):

	table = 'default_table'

	# the default option is not using `fail` feature
	use_fail = False
