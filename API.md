**本项目仍在施工中，现在本文件只会记录接口信息**

- [使用方法](#使用方法)
- [API](#api)
	- [`common.spiders.common_spider.CommonSpider`](#commonspiderscommon_spidercommonspider)
		- [`use_cookies`](#use_cookies)
	- [`common.items.common_item.CommonItem`](#commonitemscommon_itemcommonitem)
		- [`table`](#table)
		- [`use_fail`](#use_fail)

# 使用方法

可以考虑如下几种方式:
- 传参时写入值
- 子类继承父类，自定义某些字段

# API

## `common.spiders.common_spider.CommonSpider`

- `parent`: `scrapy.Spider`

### `use_cookies`

- `type`: `boolean`
- `desc`: 为`True`则为此蜘蛛启用`cookies`组件，为`False`则不启用。注意：启用的前提是在`settings`中配置了`middlewares`

## `common.items.common_item.CommonItem`

- `parent`: `scrapy.Item`

### `table`

- `type`: `str`
- `desc`: 此`Item`将被保存到的数据表

### `use_fail`

- `type`: `boolean`
- `desc`: 此`Item`是否回进行重试，或重试时是否需要删除失败记录
