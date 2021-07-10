import hashlib


def get_md5(content: str):
	print('5')
	md5_obj = hashlib.md5()
	print('7')
	md5_obj.update(content.encode())
	print('9')
	return str(md5_obj.hexdigest()).upper()
