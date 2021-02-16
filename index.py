#!/usr/bin/python3
from codeweb.htlol_api import pritn,get_contents
from urllib import request,parse
import os,cgitb,cgi,codeweb.login as login
if __name__=='__main__':
	pritn("Content-type: text/html; charset=utf-8\n\n")
	cgitb.enable()
	#Đổi Session ID (nếu có)
	f=cgi.FieldStorage()
	fv=f.getvalue('sid')
	if (fv is not None):
		m=open('codeweb/sessionid.txt','w')
		m.write(fv)
		m.close()
	fc={"username": f.getvalue('username'), "password": f.getvalue('password')}
	if (fc['username'] is not None and fc['password'] is not None):
		sessid=open('codeweb/sessionid.txt',"r").read()
		header={'Cookie':'PHPSESSID='+sessid}
		n=request.Request("http://hoc.chuyentin.pro:8002/codeweb/login.php",data=parse.urlencode(fc).encode('utf-8'),headers=header)
		r=request.urlopen(n)
	#Kết nối tới hoc.chuyentin.pro:8002 và kiểm tra loại trang
	if (f.getvalue('subm') is not None):
		login.get_page(idbai=f.getvalue('idbai'),lang=f.getvalue('lang'),formbai=f.getvalue('formbai'))
	else:
		login.get_page()
