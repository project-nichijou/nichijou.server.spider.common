import hashlib


def get_md5(content: str):
	md5_obj = hashlib.md5()
	md5_obj.update(content.encode())
	return str(md5_obj.hexdigest()).upper()
