from common.utils.formatter import format_log
from common.items.fail_request_item import CommonFailedRequestItem
from common.utils.hash import get_md5
from common.config import settings as common_settings
from common.cookies.cookies_io import read_cookies
import scrapy
import json


class CommonSpider(scrapy.Spider):
	
	name = 'default_common_spider'

	# default option of using cookies is false
	use_cookies = False


	def __init__(self, fail='false', *args, **kwargs):
		# use super class's method to initialize
		super(CommonSpider, self).__init__(*args, **kwargs)
		# call customized init method
		self.initialize()
		# define data source
		if fail == 'on' or fail == 'true' or fail == '1' or fail == True or fail == 1:
			self.init_fail_datasource()
		else:
			self.init_normal_datasource()


	# this should be implemented
	def initialize(self):
		pass


	# this should be implemented
	def init_normal_datasource(self):
		pass


	# this should be implemented
	def init_fail_datasource(self):
		pass


	def request(self, url, callback, errback, cb_kwargs=None):
		'''
		warpper for scrapy.Request
		'''
		request = scrapy.Request(url=url, callback=callback, errback=errback, cb_kwargs=cb_kwargs)
		if self.use_cookies:
			request.cookies = read_cookies()
		headers = common_settings.HEADERS
		for key in headers.keys():
			request.headers[key] = headers[key]
		return request


	def errback(self, failure):
		'''
		callback function when error happens
		'''
		request = failure.request
		parameters = request.cb_kwargs
		url = request.url
		url_md5 = get_md5(url)

		yield CommonFailedRequestItem(
			url = url,
			url_md5 = url_md5,
			spider = self.name,
			desc = format_log(
				info = 'exception caught in spider.',
				values = {
					'failure': failure.__dict__,
					'parameters': parameters
				}
			),
			params = json.dumps(parameters)
		)
