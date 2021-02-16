from codeweb.htlol_api import get_contents,get_bai,get_categories,get_link,get_submission,get_submissions,pritn
from codeweb.search import search_page
import cgi
import requests
import re
from urllib import request
from http.client import HTTPConnection,HTTPResponse
from html import escape
from random import randrange
def determine_pagetype(**args):
	g=get_contents('codeweb/upload.php')
	if g[0]==1:
		return g
	elif g[0]==0:
		f=cgi.FieldStorage()
		if (f.getvalue('req')==None):
			return (0,"Successful","")
		elif (f.getvalue('req')=='parselog'):
			if (f.getvalue("lfname")!=None):
				return (2,"Log parsing page",f.getvalue("lfname"))
			return (2,"Log searching page","")
		elif (f.getvalue('req')=='upload'):
			return (3,"Upload page","")
		elif (f.getvalue('req')=='search'):
			if (f.getvalue("round")):
				return (4,"Search page",f.getvalue("round"))
			return (4,"Search page","0")
		elif (f.getvalue('req')=='logout'):
			return (5,"Log out","")
		elif (f.getvalue('req')=='submit_upload'):
			return (6,"Submit upload",args)
		else:
			return (0,"Unknown operation","")
	else:
		return g
def get_page(**args):
	g=determine_pagetype(**args)
	if (g[0]==0):
		n=open("codeweb/index_form.html",'r',encoding='utf-8')
		r=n.read()
		p=open("codeweb/indexpage.txt",'r',encoding='utf-8')
		pr=p.read().split('\n')
		a=[i.split(', ') for i in pr]
		pritn(r%(a[0][randrange(0,len(a[0]))]+' '+a[1][randrange(0,len(a[1]))]))
	elif (g[0]==1):
		n=open("codeweb/login_form.html",'r',encoding='utf-8')
		r=n.read()
		pritn(r)
	elif (g[0]==2):
		if (g[1]=="Log searching page"):
			n=open("codeweb/log_search.html",'r',encoding='utf-8')
			s=get_submissions()
			r=n.read()
			htr=''
			for i in s[2]:
				htr+="<tr><td>%s</td><td>%s</td><td>%s</td><td><a href='?req=parselog&lfname=%s'>Xem</a></td></tr>"%(i[2],i[3],i[4],i[0])
			pritn(r%htr)
		elif (g[1]=="Log parsing page"):
			n=open("codeweb/log_parse.html",'r',encoding='utf-8')
			s=get_submission(g[2])
			r=n.read()
			htr=''
			for i in s[2][0]:
				htr+="<tr><td>"+i[2]+"</td><td class='"+("wa","ac")[i[5]=="Kết quả khớp đáp án!"]+"_res'>"+i[5]+"</td></tr>"
			pritn(r%(s[2][1]+(htr,)))
	if (g[0]==3):
		n=open("codeweb/upload.html",'r',encoding='utf-8')
		r=n.read()
		pritn(r)
	elif (g[0]==4):
		r=search_page(g[2])
		pritn(r)
	elif (g[0]==5):
		g=get_contents('codeweb/logout.php')
		pritn("<html><head></head><body><script>location='.'</script></body></html>")
	elif (g[0]==6):
		multipart={'file':(g[2]['idbai']+'.'+g[2]['lang'],g[2]['formbai'])}
		cookies={"PHPSESSID":open("codeweb/sessionid.txt").read()}
		req=requests.post("http://hoc.chuyentin.pro:8002/codeweb/upload.php",files=multipart,cookies=cookies)
		n=req.text
		r=re.compile(r"alert\(\"(.*)\"\)")
		m=r.findall(n)[0]+"<br><button onclick='window.history.back()'>Quay lại</button>"
		np=open("codeweb/index_form.html",'r',encoding='utf-8')
		rp=np.read()
		pritn(rp%m)

if __name__=='__main__':
	get_page()