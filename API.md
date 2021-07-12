**本项目仍在施工中，现在本文件只会记录接口信息**

- [使用方法](#使用方法)
- [API](#api)
	- [`common.spiders.common_spider.CommonSpider`](#commonspiderscommon_spidercommonspider)
		- [`use_cookies`](#use_cookies)
	- [`common.items.common_item.CommonItem`](#commonitemscommon_itemcommonitem)
		- [`table`](#table)
		- [`primary_keys`](#primary_keys)
		- [`_url`](#_url)
		- [`use_fail`](#use_fail)

# 使用方法

可以考虑如下几种方式:
- 子类继承父类，自定义某些字段，覆写值
- 传参使用。注意：`Item`只有变量名为`_`开始的才能够作为属性直接修改，否则需要通过`dict`的方式。

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

### `primary_keys`

- `type`: `list`
- `desc`: 存入数据表的`primary_keys` (主键)，用于`update`数据，若此项缺失，则会直接覆写

### `_url`

- `type`: `str`
- `desc`: 产生该`Item`请求的`url`，用于删除`fail`记录

### `use_fail`

- `type`: `boolean`
- `desc`: 此`Item`是否回进行重试，或重试时是否需要删除失败记录
