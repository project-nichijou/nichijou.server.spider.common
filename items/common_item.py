import scrapy


class CommonItem(scrapy.Item):

	table = 'default_table'

	primary_keys = ['default_primary_key']

	_url = ''

	# the default option is not using `fail` feature
	use_fail = False
