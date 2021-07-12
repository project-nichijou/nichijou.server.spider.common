# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from common.utils.checker import is_null
from common.database.database import CommonDatabase


class CommonStoringPipeline:

	def __init__(self):
		self.database = CommonDatabase()


	def process_item(self, item, spider):
		# judge whether has destination table
		if not hasattr(item, 'table'):
			return item
		table = item.table
		# judge whether has primary_keys
		if not hasattr(item, 'primary_keys'):
			self.database.write(table, dict(item))
		elif is_null(item.primary_keys):
			self.database.write(table, dict(item))
		else:
			self.database.update(table, item.primary_keys, dict(item))
		# judge whether use_fail
		if hasattr(item, 'use_fail'):
			if item.use_fail == True:
				self.database.delete_fail(url=item._url, spider=spider.name)
		return item
