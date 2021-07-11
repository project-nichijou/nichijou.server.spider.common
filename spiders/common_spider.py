from common.config import settings as common_settings
from common.cookies.cookies_io import read_cookies
import scrapy


class CommonSpider(scrapy.Spider):
	
	name = 'default_common_spider'

	# default option of using cookies is false
	use_cookies = False


	def request(self, url, callback, errback, cb_kwargs=None):
		'''
		warpper for scrapy.request
		'''
		request = scrapy.Request(url=url, callback=callback, errback=errback, cb_kwargs=cb_kwargs)
		if self.use_cookies:
			request.cookies = read_cookies()
		headers = common_settings.HEADERS
		for key in headers.keys():
			request.headers[key] = headers[key]
		return request
