# Dummy htlol_api in case of console execution
def pritn(st,encoding='utf-8'):
	pass
def get_contents(access_uri):
	return (2,"Please run on a web server.","")
def check_contents(access_uri):
	return (2,"Please run on a web server.","")
def get_categories():
	return (2,"Please run on a web server.","")
def get_bai(id):
	return (2,"Please run on a web server.","")
def get_submissions():
	return (2,"Please run on a web server.","")
def get_submission(sub_link):
	return (2,"Please run on a web server.","")
def get_link(f):
	return (2,"Please run on a web server.","")
class getlink_dict(dict):
	def __missing__(self,key):
		return ""
# Interface for accessing associated exercises' file types
class getlink:
	def __getitem__(self,key):
		return ""