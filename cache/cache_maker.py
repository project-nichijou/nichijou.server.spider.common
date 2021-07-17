import time
from common.utils.datetime import get_time_str_from_timestamp
from common.utils.hash import get_md5
from common.items.cache_item import CommonCacheItem
import dill
from common.cache.cache_response import CacheResponse


def make_cache_item(response, expire):
	'''
	`response`: response to be cached, \n
	`expire`: after how many seconds would expire
	'''
	# 判断当前请求是不是缓存，是的话忽略
	if not CacheResponse.judge_cache(response):
		request = response.request
		certificate = response.certificate

		response.request = None
		response.certificate = None

		CacheResponse.mark_cache(response)

		content = dill.dumps(response)

		response.request = request
		response.certificate = certificate

		return CommonCacheItem(
			url_md5 = get_md5(response.url),
			url = response.url,
			expire = get_time_str_from_timestamp(int(time.time()) + expire),
			content = content
		)
	return None
