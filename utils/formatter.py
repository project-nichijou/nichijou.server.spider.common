import traceback
from common.utils.checker import is_null
from common.utils.ac import ACAutomaton
from common.utils.hash import get_md5
from common.utils.logger import format_log
from common.database.database import CommonDatabase
import time


def format_id(id):
	if isinstance(id, int):
		return id
	elif isinstance(id, str):
		low_word = get_md5(id)[-8:]
		return int(low_word, 16)


def format_date(timestr: str, identifier=None):
	
	def get_formated_date(t):
		return time.strftime("%Y-%m-%d", t)
	
	timestr = timestr.replace(' ', '')
	if is_null(timestr): return None

	try:
		ts = time.strptime(timestr, "%Y-%m-%d")
		return get_formated_date(ts)
	except: pass
	try:
		ts = time.strptime(timestr, "%Y/%m/%d")
		return get_formated_date(ts)
	except: pass
	try:
		ts = time.strptime(timestr, "%Y年%m月%d日")
		return get_formated_date(ts)
	except: pass
	CommonDatabase().log(
		format_log(
			info = 'formatting date failed',
			values = {
				'timestr': timestr,
				'identifier': identifier
			}
		)
	)
	return None


def format_int(value: str, identifier=None):
	if is_null(value): return None
	try:
		try:
			return int(value)
		except: pass
		intstr = ''
		for c in value:
			if c.isdigit():
				intstr = f'{intstr}{c}'
			else: break
		if intstr == '': return None
		else: return int(intstr)
	except Exception as e:
		CommonDatabase().log(
			format_log(
				info = 'exception caught when formatting int',
				exception = e,
				traceback = traceback.format_exc(),
				values = {
					'value': value,
					'identifier': identifier
				}
			)
		)
		return None


def format_weekday(timestr, identifier=None):
	if is_null(timestr): return None
	try:
		if ACAutomaton([
			'星期一', '周一', '1', 'げつようび', '月曜日', '月', 'Mon', 'Monday'
			]).match(str(timestr)):
			return 1
		if ACAutomaton([
			'星期二', '周二', '2', 'かようび', '火曜日', '火', 'Tue', 'Tuesday'
			]).match(str(timestr)):
			return 2
		if ACAutomaton([
			'星期三', '周三', '3', 'すいようび', '水曜日', '水', 'Wed', 'Wednesday'
			]).match(str(timestr)):
			return 3
		if ACAutomaton([
			'星期四', '周四', '4', 'もくようび', '木曜日', '木', 'Thu', 'Thursday'
			]).match(str(timestr)):
			return 4
		if ACAutomaton([
			'星期五', '周五', '5', 'きんようび', '金曜日', '金', 'Fri', 'Friday'
			]).match(str(timestr)):
			return 5
		if ACAutomaton([
			'星期六', '周六', '6', 'どようび', '土曜日', '土', 'Sat', 'Saturday'
			]).match(str(timestr)):
			return 6
		if ACAutomaton([
			'星期日', '周日', '7', 'にちようび', '日曜日', '日', 'Sun', 'Sunday'
			]).match(str(timestr)):
			return 7
		raise Exception('unkown weekday format')
	except Exception as e:
		CommonDatabase().log(
			format_log(
				info = 'exception caught when formatting weekday',
				exception = e,
				traceback = traceback.format_exc(),
				values = {
					'weekday': timestr,
					'identifier': identifier
				}
			)
		)
		return None


def format_airing_status(status, identifier=None):
	if is_null(status): return None
	try:
		if isinstance(status, int):
			if status > 3 or status < 0: return 3
			else: return status
		if ACAutomaton([
			'Air', 'air', 'AIR', '已放送', '已完结', '已', 'end', 'End', 'END', 'OnAir', 'onAir', 'onair'
			]).match(str(status)):
			return 0
		if ACAutomaton([
			'NA', '未放送', '未', 'na'
			]).match(str(status)):
			return 1
		if ACAutomaton([
			'Today', 'today', 'TODAY', '正在放送', '正在', '即将', '即将放送', '将'
			]).match(str(status)):
			return 2
		raise Exception('unkown airing status')
	except Exception as e:
		CommonDatabase().log(
			format_log(
				info = 'exception caught when formatting airing status',
				exception = e,
				traceback = traceback.format_exc(),
				values = {
					'status': status,
					'identifier': identifier
				}
			)
		)
		return 3


def format_episode_type(type, identifier=None):
	if is_null(type): return None
	try:
		if isinstance(type, int):
			if type > 6 or type < 0: return 6
			else: return type
		if ACAutomaton([
			'本篇', '正片'
			]).match(str(type)):
			return 0
		if ACAutomaton([
			'SP', '特别篇', 'Special', 'sp', 'special'
			]).match(str(type)):
			return 1
		if ACAutomaton([
			'OP', '片头曲', '头', 'op', 'open', 'Open'
			]).match(str(type)):
			return 2
		if ACAutomaton([
			'ED', '片尾曲', '尾', 'end', 'End', 'ed'
			]).match(str(type)):
			return 3
		if ACAutomaton([
			'PV', 'CM', 'pv', 'cm', 'preview', 'commercial'
			]).match(str(type)):
			return 4
		if ACAutomaton([
			'MAD', 'mad'
			]).match(str(type)):
			return 5
		if ACAutomaton([
			'Unknown', 'unknown', '未知'
			]).match(str(type)):
			return 6
		raise Exception('unkown episode type')
	except Exception as e:
		CommonDatabase().log(
			format_log(
				info = 'exception caught when formatting episode type',
				exception = e,
				traceback = traceback.format_exc(),
				values = {
					'type': type,
					'identifier': identifier
				}
			)
		)
		return 6



def format_duration(duration: str, identifier=None):
	if is_null(duration): return None
	try:
		time_list = [0, 1, 60, 3600, 86400]

		def get_key_duration(key: str, index: int):
			if ACAutomaton(['h', 'H', '时']).match(str(key)):
				return time_list[3]
			if ACAutomaton(['m', 'M', '分']).match(str(key)):
				return time_list[2]
			if ACAutomaton(['s', 'S', '秒']).match(str(key)):
				return time_list[1]
			return time_list[index]
		
		int_str = ''
		t_str = ''
		last_is_int = False
		sep = []
		
		for c in duration:
			if c.isdigit():
				if not last_is_int and t_str != '':
					sep.append((False, t_str))
					t_str = int_str = ''
				int_str = f'{int_str}{c}'
				last_is_int = True
			else:
				if last_is_int and int_str != '':
					sep.append((True, int_str))
					t_str = int_str = ''
				t_str = f'{t_str}{c}'
				last_is_int = False
		if not last_is_int and t_str != '':
			sep.append((False, t_str))
		if last_is_int and int_str != '':
			sep.append((True, int_str))

		if len(sep) == 0: return None
		if len(sep) == 1 and not sep[0][0]: return None

		start_index = 0
		if not sep[0][0]: start_index = 1

		res = 0

		time_dict_index = (len(sep) - start_index + 1) // 2

		for i in range(start_index, len(sep), 2):
			if i + 1 == len(sep):
				res += int(sep[i][1])
				break
			num = int(sep[i][1])
			key = sep[i + 1][1]
			
			res += get_key_duration(key, time_dict_index) * num
			time_dict_index -= 1
		return int(res)
	except Exception as e:
		CommonDatabase().log(
			format_log(
				info = 'exception caught when formatting duration',
				exception = e,
				traceback = traceback.format_exc(),
				values = {
					'duration': duration,
					'identifier': identifier
				}
			)
		)
		return None
