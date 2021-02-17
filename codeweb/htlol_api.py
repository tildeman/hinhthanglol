from urllib import request,error as uerror
import sys
import re

def pritn(st,encoding='utf-8'):
	sys.stdout.buffer.write(bytes(st,encoding=encoding))
def get_contents(access_uri):
	sessid=open('codeweb/sessionid.txt',"r").read()
	header={'Cookie':'PHPSESSID='+sessid}
	n=request.Request('http://hoc.chuyentin.pro:8002/'+access_uri,headers=header)
	try:
		m=str(request.urlopen(n).read(),encoding='utf-8')
	except uerror.HTTPError as e:
		return(1,str(e)+" Error",e.code)
	return(0,"Successful",m)
def check_contents(access_uri):
	n=request.Request('http://hoc.chuyentin.pro:8002/'+access_uri)
	try:
		request.urlopen(n).read()
	except uerror.HTTPError as e:
		return(1,str(e)+" Error",e.code)
	return(0,"Successful","")
def get_categories():
	g=get_contents('index.php')
	if (g[0]!=0):
		return g
	r=re.compile(r"<option value=\"(\d+)\"   >\d* \- ([^<^>]*)</option>")
	a=r.findall(g[2])
	return(0,"Successful",a)
def get_bai(idbai):
	g=get_contents('codeweb/logs.php?idvong='+idbai+"&tab=rank")
	if (g[0]!=0):
		return g
	r=re.compile(r"<td>&nbsp &nbsp (\w+) &nbsp &nbsp</td>")
	a=r.findall(g[2])
	return(0,"Successful",a)
def get_submissions():
	g=get_contents('contests/NopOnline/Logs/DEL/')
	r=re.compile(r"<tr><td valign=\"top\"><img src=\"/icons/text\.gif\" alt=\"\[TXT\]\"></td><td><a href=\"((\d*)%5b([a-zA-Z0-9_]*)%5d%5b([a-zA-Z0-9]*)%5d\.([a-zA-Z0-9]*)\.log)\">\2\[\3]\[.*&gt;</a></td><td align=\"right\">\d\d\d\d-\d\d-\d\d \d\d:\d\d  </td><td align=\"right\">[K0-9\. ]*</td><td>&nbsp;</td></tr>")
	a=r.findall(g[2])
	g2=get_contents('contests/NopOnline/Logs/')
	a2=r.findall(g2[2])
	return(0,"Successful",a+a2)
def get_submission(sub_link):
	g=get_contents('contests/NopOnline/Logs/DEL/'+sub_link)
	if (g[0]==1):
		g=get_contents("contests/NopOnline/Logs/"+sub_link)
	ra=re.compile(r"([a-zA-Z0-9]*)‣([a-zA-Z0-9]*)‣[a-zA-Z\$]*([0-9]*): ([0-9\.]*)(\r\nThời gian ≈ [0-9\.]* giây)?\r\n(.*)\r",re.MULTILINE)
	a=ra.findall(g[2])
	rb=re.compile(r"([a-zA-Z0-9_]+)‣([a-zA-Z0-9]+): (.*)\r\n\2\.([a-zA-Z]*)",re.MULTILINE)
	b=rb.search(g[2])
	return(0,"Successful",(a,b.groups()))
def get_link(f):
	r='.png'
	n=check_contents("contests/test/"+f+'/'+f+r)
	if (n[0]==1):
		r='.pdf'
	return (0,"Successful",r)


# Generic mapping type for link objects
class getlink_dict(dict):
	def __missing__(self,key):
		rv=get_link(key)
		n=open("codeweb/accmode.txt","a")
		n.write(key+" "+rv[2]+"\n")
		return rv[2]

# Interface for accessing associated exercises' file types
class getlink:
	def __init__(self):
		self.linkext=getlink_dict([a.split() for a in open("codeweb/accmode.txt").read().splitlines()])
	def __getitem__(self,key):
		return self.linkext[key]
