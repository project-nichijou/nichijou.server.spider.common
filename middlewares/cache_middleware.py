from common.utils.checker import is_null
import traceback
from common.utils.logger import format_log
from common.database.database import CommonDatabase
from scrapy import signals


class CommonCacheMiddleware:
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the downloader middleware does not modify the
	# passed objects.

	database = CommonDatabase()

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_request(self, request, spider):
		# Called for each request that goes through the downloader
		# middleware.
		try:
			url = request.url
			cache = self.database.read_cache(url=url)
			if is_null(cache): return None
			cache.request = request
			return cache
		except Exception as e:
			self.database.log(
				format_log(
					info = 'exception caught in cachemiddleware',
					exception = e,
					traceback = traceback.format_exc(),
					values = {
						'spider': spider.name,
						'url': request.url
					}
				)
			)
		# Must either:
		# - return None: continue processing this request
		# - or return a Response object
		# - or return a Request object
		# - or raise IgnoreRequest: process_exception() methods of
		#   installed downloader middleware will be called
		return None

	def process_response(self, request, response, spider):
		# Called with the response returned from the downloader.
		# Must either;
		# - return a Response object
		# - return a Request object
		# - or raise IgnoreRequest
		return response

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)
