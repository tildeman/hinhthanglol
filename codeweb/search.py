from codeweb.htlol_api import get_categories,get_bai,getlink
def search_page(id=0):
	g=get_categories()
	gl=getlink()
	r1=''.join(map(lambda x:"<option value='"+x[0]+"' "+("selected" if x[0]==id else "")+">"+x[1]+"</option>",g[2]))
	if (id!=0):
		b=get_bai(id)
		r2=''.join(map(lambda x: "<option value='"+x+"/"+x+gl[x]+"'>"+x+"</option>",b[2]))
	else:
		r2=""
	nf=open("codeweb/search_form.html","r",encoding='utf-8')
	nr=nf.read()
	n=nr%(r1,r2)
	return n