from common.utils.logger import format_log
from common.items.fail_request_item import CommonFailedRequestItem
from common.utils.hash import get_md5
from common.config import settings as common_settings
from common.cookies.cookies_io import read_cookies
import scrapy


class CommonSpider(scrapy.Spider):
	
	name = 'default_common_spider'

	# default option of using cookies is false
	use_cookies = False


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
		urlmd5 = get_md5(url)

		yield CommonFailedRequestItem(
			url = url,
			urlmd5 = urlmd5,
			spider = self.name,
			desc = format_log(
				info = 'exception caught in spider.',
				values = {
					'failure': failure
				})
		)
