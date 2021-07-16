import scrapy.http.response


class CacheResponse(scrapy.http.response.Response):

	is_cache = False

	def mark_cache(self):
		self.is_cache = True
		return self


	def judge_cache(self):
		if not hasattr(self, 'is_cache'):
			return False
		return self.is_cache
