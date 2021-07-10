import json

def read_cookies():
	try:
		with open('./common/cookies/cookies.json', 'r', encoding='utf-8') as f:
			return json.load(f)
	except: return {}

def write_cookies(cookies):
	json.dump(cookies, open('./common/cookies/cookies.json', 'w', encoding='utf-8'), ensure_ascii=False)
